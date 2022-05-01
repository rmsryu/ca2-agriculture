from math import inf
import tweepy
import numpy as np
import pandas as pd

class ProcessTweets():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, environment="development", bearerToken = "AAAAAAAAAAAAAAAAAAAAABoHcAEAAAAA78rV2Phg2vUbwTdcJ2QPGGji65M%3DsTr8DETODttIuwkHy9czi663YUpUPLDOVY2VqUzmBdshiJmLT3" ):
        """_summary_

        Args:
            environment (str, optional): _description_. Defaults to "development".
            bearerToken (str, optional): _description_. Defaults to "AAAAAAAAAAAAAAAAAAAAABoHcAEAAAAA78rV2Phg2vUbwTdcJ2QPGGji65M%3DsTr8DETODttIuwkHy9czi663YUpUPLDOVY2VqUzmBdshiJmLT3".
        """        
        #api_key = "Y0hENmxMwkILuxxY0yb9NHG0L"
        #api_secret = "33OSFPPFNWlN3S9CvL5ok4ClBLjUdviC4zzpLs9aRBwJVzHPMA"
        auth = tweepy.OAuth2BearerHandler(bearerToken)
        
        self.environment=environment
        self.api = tweepy.API(auth)
    
    def SearchTweets(self, query:str,  processQuote = False, limit=inf):
        """ Search Tweets in the last 7 days

        Args:
            query (str): Twitter API V2.0 https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query
        """        
        return self.GetDataFrame(tweepy.Cursor(self.api.search_tweets,q=query).items(limit), processQuote)

    def Search30Day(self, query:str, processQuote = False,  environment = "development", limit=inf):
        """Search last 30 days

        Args:
            query (str): Twitter API V2.0 https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query
            fromDate (str, optional): From Date Filter. Defaults to "202201010000".
            toDate (str, optional): To Date Filter. Defaults to "202204300000".
            environment (str, optional): Sandbox Environment. Defaults to "development".
        """ 
        return self.GetDataFrame(
                    tweepy.Cursor(
                        self.api.search_30_day,
                        label=environment,
                        query=query
                    ).items(limit), processQuote)

    def SearchFull(self, query:str, processQuote = False, fromDate = "202201010000", toDate = "202204300000", environment = "development", limit=inf):
        """Full search since 2006

        Args:
            query (str): Twitter API V2.0 https://developer.twitter.com/en/docs/twitter-api/tweets/counts/integrate/build-a-query
            fromDate (str, optional): From Date Filter. Defaults to "202201010000".
            toDate (str, optional): To Date Filter. Defaults to "202204300000".
            environment (str, optional): Sandbox Environment. Defaults to "development".
        """ 
        return self.GetDataFrame(
            tweepy.Cursor(
                    self.api.search_full_archive,
                    label=environment,
                    query=query,
                    fromDate=fromDate,
                    toDate=toDate
                ).items(limit), processQuote)

    def GetDataFrame(self, 
        tweets:tweepy.Cursor, 
        processQuote = False,
        columns = ["id","geo","coordinates","reply_count","favorite_count", "place", "text" ,"user.location", "place.bounding_box.type", "place.bounding_box.coordinates"]):
        
        tweets_pd = pd.json_normalize([t._json for t in tweets])
        # Replace truncated with extended text
        tweets_pd["text"] = tweets_pd.apply(lambda r: r["extended_tweet.full_text"] if r["truncated"] else r["text"], axis=1)
        
        
        # Status tweets
        tweets_status_pd = tweets_pd[[c for c in tweets_pd.columns if not(c.startswith("quoted"))]]
        tweets_status_pd.rename({"place.full_name":"place"}, axis=1, inplace=True)

        # Create 2 dataframes one for Status one for Quoted Status and merge them
        if(processQuote and ("quoted_status.text" in tweets_pd.columns)):
            #Update quoted_status text
            tweets_pd["quoted_status.text"] = tweets_pd.apply(lambda r: r["quoted_status.extended_tweet.full_text"] if r["quoted_status.truncated"] else r["quoted_status.text"], axis=1)

            # Quote status tweets
            tweets_quoted_status_pd = tweets_pd[tweets_pd["is_quote_status"]][tweets_pd.columns[tweets_pd.columns.str.startswith("quoted")]]
            # rename columns
            tweets_quoted_status_pd.rename(mapper=lambda c: c.replace("quoted_status.",""), axis='columns', inplace=True)

            # add dummy "place.bounding_box.type" and "place.bounding_box.coordinates"
            tweets_quoted_status_pd["place.bounding_box.type"] = None
            tweets_quoted_status_pd["place.bounding_box.coordinates"] = None

            arr1 = tweets_quoted_status_pd[columns].to_numpy()
            arr2 = tweets_status_pd[columns].to_numpy()
            return pd.DataFrame(np.concatenate((arr1,arr2), axis=0), columns = columns)

        return tweets_status_pd



