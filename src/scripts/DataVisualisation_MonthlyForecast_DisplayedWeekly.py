import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date
import datetime
import matplotlib.ticker as mticker

#Rainfall data for every day of the year this year
df1 = pd.read_csv("./Rainfall_Sydney_2018_Data.csv", usecols = ["Year", "Month", "Day", "Rainfall amount (millimetres)"])
df2 = pd.read_csv("C:/Users/eaderman/Downloads/Sydney_Rainfall_Data_2019.csv", usecols = ["Year", "Month", "Day", "Rainfall amount (millimetres)"])

# Make a column for the Date out of Year, Month and Day
df1['Date'] = pd.to_datetime(df1[['Year', 'Month', 'Day']])
df2['Date'] = pd.to_datetime(df2[['Year', 'Month', 'Day']])
ave_2018 = df1["Rainfall amount (millimetres)"].mean()
ave_weekly_2018 = ave_2018*7 

# Next 28 days forecast, displayed by week
Week1 = df2['Rainfall amount (millimetres)'].iloc[-69:-62].sum()
Week2 = df2['Rainfall amount (millimetres)'].iloc[-62:-55].sum()
Week3 = df2['Rainfall amount (millimetres)'].iloc[-55:-48].sum()
Week4 = df2['Rainfall amount (millimetres)'].iloc[-48:-41].sum()

x = ["Week 1", "Week 2", "Week 3", "Week 4"]
y = [Week1, Week2, Week3, Week4]
plt.axhline(y=ave_weekly_2018, color='#7fcdbb', linestyle='dashed', label='Average weekly rainfall in Sydney 2018')
plt.ylabel("Rainfall by Week over the next Month (millimetres)")
plt.xlabel("Week from Today")
plt.bar(x,y, align='center', color='#43a2ca')
plt.text(0.90,19.50, "Average weekly rainfall in Sydney 2018", style='italic')
plt.show() 

'''
fig = px.line(df2, x='Date', y='Rainfall amount (millimetres)')
fig.show() 
'''
'''
today = date.today()
print(today)
print(df2.iat[2,4])
print (date.today() - datetime.timedelta(days=1))
quit()
#Plot just the last few days 
'''
#print (today - df2.iat[2,4])
'''
time = df2['Date'].iloc[-7:]
print(time)
ave = np.ones(7)*float(412.8/365)
print(ave) 
'''

'''
eek1 = df2['Rainfall amount (millimetres)'].iloc[-38:-31].sum()
Week2 = df2['Rainfall amount (millimetres)'].iloc[-30:-23].sum()
Week3 = df2['Rainfall amount (millimetres)'].iloc[-22:-15].sum()
Week4 = df2['Rainfall amount (millimetres)'].iloc[-14:-7].sum()

x = ["7 Days", "14 Days", "21 Days", "28 Days"]
y = [Week1, Week2, Week3, Week4]
plt.axhline(y=ave_weekly, color='r', linestyle='dashed', label='Average weekly rainfall in Sydney 2018')
ax.set_ylabel("Rainfall amount (millimetres)")
ax.set_xlabel("Days from Today")
plt.plot(x,y) 
plt.show() 
'''
 
