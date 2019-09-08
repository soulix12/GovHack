import pandas as pd
import numpy as np


'''DATA''' 
# Rainfall data for Sydney Observatory for every day this year so far
df1 = pd.read_csv("./Rainfall_Sydney_2018_Data.csv", usecols = ["Year", "Month", "Day", "Rainfall amount (millimetres)"])
df2 = pd.read_csv("C:/Users/eaderman/Downloads/Sydney_Rainfall_Data_2019.csv", usecols = ["Year", "Month", "Day", "Rainfall amount (millimetres)"])

'''DECISION MAKING FOR SUGGESTIONS BASED ON CRITERIA'''
# Dam levels low, rainfall expected in next 7 days - save water! 
current_dam = 0.507 #placeholder data 
#ave_rain_forecast = average of rainfall forecasted over next 7 days over Warragamba 

if ((current_dam < 0.50) and (ave_rain > 0.5)):
    print("Dam levels are low! Reduce water usage by turning off running taps, reducing shower time")
else:
    print("Dam levels are decent!")

# Average daily rainfall in your area is high, then install rainwater tank
ave_2018 = df1["Rainfall amount (millimetres)"].mean()
ave_weekly_2018 = ave_2018*7
ave_daily_rain = df2["Rainfall amount (millimetres)"].mean()

if (ave_daily_rain > ave_2018):
    print("Your regional rainfall is above the national average! Consider installing a rainwater tank.")
else:
    print("Your regional rainfall is below the national average! You rely primarily on your local dam for your water.")



    

