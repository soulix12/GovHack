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
#print(df1.head())
#print(ave_2018, ave_weekly_2018)

#ave = float(1000.2/365) #Sydney total for 2018 is 1000.2 mm
#ave_weekly = ave*7 #This is a weekly average rainfall for Sydney in 2018

# Next 7 days forecast 
ax = df2.iloc[-69:-62].plot(kind='bar', x='Date', y='Rainfall amount (millimetres)', color='#43a2ca', legend=False) 
ax.plot(legend=None)
plt.axhline(y=ave_2018, color='#7fcdbb', linestyle='dashed') 
ax.set_ylabel("Rainfall (millimetres)")
#ax.set_ylim([-0.05,3.50])
ax.set_xlabel("2019")
ticklabels = ['']*len(df2.iloc[-69:-62])
ticklabels[::1] = df2['Date'].iloc[-69:-62].dt.strftime('%b %d')
ax.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
plt.gcf().autofmt_xdate()
ax.text(-0.20,3.30, "Average daily rainfall in Sydney 2018", style='italic')
plt.show()

'''
# Next 31 days forecast based on weekly rainfall - can't remove legend for columns
ax = df2.iloc[-38:-7].plot(kind='bar', x='Date', y='Rainfall amount (millimetres)', color='b') 
ax.set_xlabel("Date")
plt.axhline(y=ave_weekly, color='r', linestyle='dashed', label='Average weekly rainfall in Sydney 2018')
ax.set_ylabel("Rainfall amount (millimetres)")
ax.legend()
ticklabels = ['']*len(df2.iloc[-38:-7])
ticklabels[::7] = df2['Date'].iloc[-38:-7:7].dt.strftime('%b %d\n%Y')
ax.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
#plt.xticks(np.arange(df2['Date'].iat[5,-38], df2['Date'].iat[5,-7], 7))
plt.gcf().autofmt_xdate()
plt.show() 
'''

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
 
