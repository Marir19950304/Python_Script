import tweepy
import pandas as pd
import os

consumer_key = "xrRIfKFh7pwrVDd85LM0bTyQ8"
consumer_secret = "2JixcFtk5AsmGpFlQhH9gzGfbKAad9rLRWAveZJRUEBgz9yfkI"
access_token = "1456224104986595331-qMjvgL1j4Gv1NXxZjjEpwzQJCji1EI"
access_token_secret = "Eh1X2XGCvrHufnR0sN5bVJKrW4yLwzAvwitZ7GhLl7z3k"


class Streamer(tweepy.Stream):

    def on_status(self, status):
        print("AAAAAAAAAAAAAAAA")
        if hasattr(status, "extended_tweet"):
            text = status
        else:
            text = status
        tmp_data = status._json
        df_tmp = pd.DataFrame([tmp_data])
        if os.path.isfile("tweets.csv"):
          df = pd.read_csv('tweets.csv')
        else:
          df = pd.DataFrame()
        df = df.append(df_tmp)
        df.to_csv('tweets.csv', index=False)



        print("tweet extracted...")

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        pass


stream_listener = Streamer(consumer_key,consumer_secret,access_token, access_token_secret)
stream_listener.filter(track=['#corona'])
