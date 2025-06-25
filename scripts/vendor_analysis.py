import pandas as pd
import matplotlib.pyplot as plt
class vendor:
    def __init__(self , path):
        try:
            self.df =  pd.read_csv(path)
            self.df["date"] = pd.to_datetime(self.df["date"])
            self.df["week"] = self.df["date"].dt.isocalendar().week
            self.df = self.df[self.df["message"].str.strip() != ""]
        except:
            print("Could Not read the file")

    
    def  Statics_view(self , channel_name):
        print("**Statics of channels view**")
        stat = self.df[self.df["channel"]== channel_name]["views"].describe()
        print(stat)
    
    def post_frequencey(self , channel_name):
        grouped = self.df[self.df["channel"]== channel_name ].groupby("week")
        grouped.size().plot( ylabel="Frequency", title = "Number of posts per week")
        plt.show()
        Posting_Frequency= grouped.size().mean()
        return Posting_Frequency

    def average_views(self , channel_name):
         Avg_Views = self.df[self.df["channel"]== channel_name]["views"].mean()
         grouped = self.df[self.df["channel"]== channel_name ].groupby("week")
         grouped["views"].sum().plot( ylabel="Total view", title = "Total Number of Views per week")
         plt.show()
         return Avg_Views
    def score(self , Posting_Frequency , Avg_Views):
        Score = (Avg_Views * 0.5) + (Posting_Frequency * 0.5) 
        return Score
    def max_view_message(self , channel):
        max_view =  self.df[
        (self.df["channel"] == channel)]["views"].max()
        message = self.df[
          (self.df["channel"] == channel) &
          (self.df["views"] == max_view)
         ]["processed_text"].value_counts() 
        print(message)
 