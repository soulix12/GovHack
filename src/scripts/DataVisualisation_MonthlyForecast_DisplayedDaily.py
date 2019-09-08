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

# Next 31 days forecast based on weekly rainfall 
ax = df2.iloc[-69:-38].plot(kind='bar', x='Date', y='Rainfall amount (millimetres)', color='#43a2ca', legend=False) 
ax.plot(legend=None)
plt.axhline(y=ave_2018, color='#7fcdbb', linestyle='dashed')
ax.set_ylabel("Rainfall (millimetres)")
ax.set_xlabel("2019")
ticklabels = ['']*len(df2.iloc[-69:-38])
ticklabels[::7] = df2['Date'].iloc[-69:-38:7].dt.strftime('%b %d')
ax.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
#plt.xticks(np.arange(df2['Date'].iat[5,-38], df2['Date'].iat[5,-7], 7))
plt.gcf().autofmt_xdate()
ax.text(7.50,3.30, "Average daily rainfall in Sydney 2018", style='italic')
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
 
