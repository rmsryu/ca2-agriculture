
from tokenize import String
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pingouin as pg
from scipy import stats 
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp as mc
import statsmodels.api as sm
from IPython.display import display, Markdown

columns_dic = {
    #index
    "crop_production_idx":                        "Crops Production Index",
    "avg_import_idx":                             "Cereals Import Index",
    "avg_export_idx":                             "Cereals Export Index",
    "gross_value_added":                          "Gross Value Added (GVA)",
    # Crops and cerelas
    "crop_mean_residues_kg":                      "Crops Residues (Kg)",
    "crop_land_use_1000ha":                       "Crop land use x 1000ha",
    "cereals_produce_price_usd_tonne":            "Cereals Produce Price ($/tonne)",
    "total_subsides_on_field_crops":              "Subsides on Field Crops",
    "prod_cereals_real_price":                    "Cereals Value at Real Price",
    # Employment
    "employment_ratio_rural_areas_pct":           "% Employment Rural Areas",
    "female_employment_ratio_rural_areas_pct":    "% Female Employment Rural Areas",
    "male_employment_ratio_rural_areas_pct":      "% Male Employment Rural Areas",
    "mean_weekly_working_hours":                  "Avg. Work (hours/week) Rural Areas",
    "female_mean_weekly_working_hours":           "Avg. Female Work (hours/week) Rural Areas",
    "male_mean_weekly_working_hours":             "Avg. Male Work (hours/week) Rural Areas",
    # Agriculture
    "agri_energy_use_tj":                         "Agr. Energy use (Terajoule)",
    # Land
    "total_uaa_ha":                               "Total Utilised Agricultural Area (ha)",
    "pct_rented_land_of_uaa":                     "% Rented land of UAA",
    "rented_land_ha":                             "Rented UAA (ha)",
    "rent_paid":                                  "Rent paid (€)",
    # Salaries
    "compensation_of_employees":                  "Salary gross (pre-tax)",
    "wages_and_salaries":                         "Wages"
}


def anova_result(dataset : pd.DataFrame, variable: String, ols_query: String, print_report = False, force_results = False):
    """Runs Anova test for the selected variable on the group for a knowing set of contries
       Assumptions for ANOVA must be satisfied before running this function.

    Args:
        dataset (pd.DataFrame): Agricultural Dataframe
        variable (String): variable in suty
        ols_query (String): ols query for ANOVA
        print_report (bool, optional): Print report in standar output. Defaults to False.
        force_results (bool, optional): Force return results. Defaults to False.

    Returns:
        (pvalue,[[]]): returns Result of ANOVA and Post Hoc analysis within groups (2D array)
    """      
    df_results = pd.DataFrame()
    model = ols(ols_query, data = dataset).fit()
    aov2 = sm.stats.anova_lm(model, type=2)
    
    ### Post hoc for the 6 countries
    comp = mc.MultiComparison(dataset[variable], dataset['country'])
    post_hoc_res = comp.tukeyhsd()
    result = post_hoc_res.summary()
    f = post_hoc_res.plot_simultaneous(comparison_name="IE",ylabel="Country",xlabel=columns_dic.get(variable))\
        .savefig(f"../visualizations/01_stats_anova_meanplot_{variable}.png");
    
    df_results = pd.DataFrame(result.data)
    new_header = df_results.iloc[0]
    df_results = df_results[1:]
    df_results.columns = new_header
    
    if(print_report):
        variable_name = columns_dic.get(variable)  if (variable in columns_dic.keys()) else variable

        print("")
        print("")
        print("[BEGIN]")
        print(f"=================================================================================")
        print(f"{variable}")
        print(f"=================================================================================")
        print(model.summary())
        print(aov2)
        if(aov2["PR(>F)"].country > 0.05 or force_results == True):
            if(aov2["PR(>F)"].country > 0.05):
                display(Markdown("<span style='color:green'>H0 ACCEPT, all means are the same</span>"))

            print(f"======================================================")
            print(f"Summary countries with {variable_name} have same means")
            print(f"======================================================")
            print(df_results.query("reject == False and (group1 == 'IE' or group2 == 'IE')")[["group1","group2"]])
            print("")
        else:
            display(Markdown("<span style='color:red'>H0 REJECT, means are not the same</span>"))
        print("[END REPORT]")
        print("")
        print("")
    
    return (aov2["PR(>F)"].country, df_results)

def anova_paircomparison_ireland_oms(data: pd.DataFrame, variables: np.array, plot_simultaneous = False):
    """Full ANOVA analsys comparison. Normality and Homoscedasticite of the variance will be check.
       Generates a report of the differentes countries and variables with Ireland as the baseline.

    Args:
        data (pd.DataFrame): Agricultural DataFrame
        variables (np.array): List of variables in study
        plot_simultaneous (bool, optional): Plot Simultaneous mean varirance comparison with Ireland as baseline. Defaults to False.

    Returns:
        _type_: _description_
    """    
    results = [["country","variable","anova_score"]]
    for variable in variables:
        if(variable == "country"):
            continue
        if(variable == "year"):
            continue
            
        print("=======================================================================")
        print(f"                           {variable}                                 ")
        print("=======================================================================")
        c_normal_dist = [[]]
        for c in data.country.unique():
            X = data.query(f"country=='{c}'")[variable]
            stat, pvalue = stats.shapiro(X)
            if(pvalue > 0.05):
                if(c_normal_dist[0] == []):
                    c_normal_dist[0] = [c,pvalue]
                else:
                    c_normal_dist.append([c,pvalue])


        similar_countries = np.array(c_normal_dist)[:,0]

        #Homogeinity of variance between countries with Ireland for GVA: Levene's test
        arr = [[]]
        count = 0
        for c in similar_countries:
            if(c == 'IE'):
                continue;
            countries = ['IE', c]

            ds = data.query("country in @countries")
            levenes_result = pg.homoscedasticity(ds, dv=variable, group='country', method='levene')
            if(arr[0] == []):
                arr[0] = list(np.append(levenes_result.values.flatten(),[variable, c]))
            else:
                arr.insert(count,list(np.append(levenes_result.values.flatten(),[variable, c])))
            count += 1

        levene_df = pd.DataFrame(arr,columns=["W","pvalue","equal_var","variable","country"])


        # Results of countries
        levene_df.query("equal_var == True")

        similar_countries = list(levene_df.query("equal_var == True").country.unique())
        similar_countries.append('IE')

        # Run anova report for all valid countries
        print(f"Candidates for ANOVA {similar_countries}")
        dataset = data.query("country in @similar_countries")

        model = ols(f"{variable}~country", data = dataset).fit()
        #print(model.summary())
        aov2 = sm.stats.anova_lm(model, type=2)
        print(aov2)
        if(aov2["PR(>F)"].country > 0.05):
            results.append([c,variable,aov2["PR(>F)"].country])

        comp = mc.MultiComparison(dataset[variable], dataset['country'])
        post_hoc_res = comp.tukeyhsd()
        result = post_hoc_res.summary()
        if(plot_simultaneous):
            f = post_hoc_res.plot_simultaneous(comparison_name="IE",ylabel="Country",xlabel=columns_dic.get(variable)) \
                .savefig(f"../visualizations/01_stats_anova_meanplot_{variable}.png");
    return results
    

def kruskal_report(dataset: pd.DataFrame, variable: String):
    """Kruskal–Wallis one-way analysis of variance

    Args:
        dataset (pd.DataFrame): Agricultural Dataset
        variable (String): variable in study

    Returns:
        _type_: _description_
    """ 
    print("")
    print("")
    print("[BEGIN]")
    print(f"=================================================================================")
    print(f"{variable}")
    print(f"=================================================================================")

    ### Post hoc for the 6 countries
    comp = mc.MultiComparison(dataset[variable], dataset['country'])
    K = comp.kruskal()
    if(K > 0.05):
        display(Markdown("<span style='color:green'>H0 ACCEPTED</span>"))
        print(f"there is no differences in means of the variable within the countries")
        print("")
    return K

def plot_normal_dist(X: np.array, title="", save_to_file = ""):
    """Normal Distribution check. 
        Axis 1  Histogram with fit to Normal Distribution on axis 1. 
        Axis 2 generates a Probablity Plot and fit of values.

    Args:
        X (np.array): Data Series
        title (str, optional): Title of the histogram. Defaults to "".
        save_to_file (str, optional): Indicates if plot needs to be saved. Defaults to "".

    Returns:
        _type_: _description_
    """    
    normallity_test_result = ""
    stat, pvalue = stats.shapiro(X)
    normallity_test_result = f"Shapiro-Wilk test pvalue: {pvalue}"
        
    
    fig = plt.figure(figsize=(10, 5), dpi=80)
    fig.add_subplot(121)
    #X = dcc_geo_df.safety_index.to_numpy();
    mu, sigma = stats.norm.fit(X);

    # Plot the histogram.

    plt.hist(X, bins=10, density=True, alpha=0.6, color='g');

    # Normal Distribution: Plot the PDF.
    xmin, xmax = plt.xlim();
    x = np.linspace(xmin, xmax, 20);
    p = stats.norm.pdf(x, mu, sigma);

    if title != "":
        title = "{:}\nFit Values: mu {:.2f} and sigma {:.2f}".format(title, mu, sigma);
    else:
        title = "Fit Values: mu {:.2f} and sigma {:.2f}".format(mu, sigma);

    plt.plot(x, p, 'r', linewidth=2, label="Normal Distribution",)
    plt.title(title);

    ax2 = fig.add_subplot(122)
    stats.probplot(X, plot=ax2, dist=stats.norm)
    plt.title("Probability Plot for Normal\n{:}".format(normallity_test_result))

    if save_to_file != "":
        plt.savefig(save_to_file)
    plt.show()
    return pvalue