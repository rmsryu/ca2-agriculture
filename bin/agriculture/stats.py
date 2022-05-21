
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pingouin as pg
import seaborn as sns;
from scipy import stats 
from scipy.stats import f_oneway
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


def anova_report(dataset, variable, ols_query, force_results = False):    
    df_results = pd.DataFrame()
    print("")
    print("")
    print("[BEGIN]")
    print(f"=================================================================================")
    print(f"{variable}")
    print(f"=================================================================================")
    model = ols(ols_query, data = dataset).fit()
    print(model.summary())
    aov2 = sm.stats.anova_lm(model, type=2)
    print(aov2)

    ### Post hoc for the 6 countries
    comp = mc.MultiComparison(dataset[variable], dataset['country'])
    post_hoc_res = comp.tukeyhsd()
    result = post_hoc_res.summary()
    f = post_hoc_res.plot_simultaneous(comparison_name="IE",ylabel="Country",xlabel=columns_dic.get(variable))\
        .savefig(f"../visualizations/01_stats_anova_meanplot_{variable}.png");
    
    if(aov2["PR(>F)"].country > 0.05 or force_results == True):
        if(aov2["PR(>F)"].country > 0.05):
            display(Markdown("<span style='color:green'>H0 ACCEPT, all means are the same</span>"))
            
        print(result)
        df_results = pd.DataFrame(result.data)
        new_header = df_results.iloc[0]
        df_results = df_results[1:]
        df_results.columns = new_header
        variable_name = columns_dic.get(variable)  if (variable in columns_dic.keys()) else variable
        print(f"======================================================")
        print(f"Summary countries with {variable_name} have same means")
        print(f"======================================================")
        print(df_results.query("reject == False and (group1 == 'IE' or group2 == 'IE')")[["group1","group2"]])
        print("")
    else:
        print("\r\nREJECT H0, At least 1 group has differences on the means\r\n")        
    print("[END REPORT]")
    print("")
    print("")
    
    return df_results


def anova_result(dataset, variable, ols_query, print_report = False, force_results = False,):    
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

def kruskal_report(dataset, variable, ols_query):
    
    df_results = pd.DataFrame()
    print("")
    print("")
    print("[BEGIN]")
    print(f"=================================================================================")
    print(f"{variable}")
    print(f"=================================================================================")
    model = ols(ols_query, data = dataset).fit()
    print(model.summary())
    aov2 = sm.stats.anova_lm(model, type=2)
    print(aov2)

    ### Post hoc for the 6 countries
    comp = mc.MultiComparison(dataset[variable], dataset['country'])
    K = comp.kruskal()
    if(K > 0.05):
        display(Markdown("<span style='color:green'>H0 ACCEPTED</span>"))
        print(f"there is no differences in means of the variable within the countries")
        print("")
    return K

def plot_normal_dist(X: np.array, title="", save_to_file = ""):
    
    normallity_test_result = ""
    stat, pvalue = stats.shapiro(X)
    normallity_test_result = f"Shapiro-Wilk test pvalue: {pvalue}"
        
    
    fig = plt.figure(figsize=(10, 5), dpi=80)
    ax1 = fig.add_subplot(121)
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