import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date
import datetime
import matplotlib.ticker as mticker

#df1 = pd.read_excel("C:/Users/eaderman/Downloads/46100do004_201617.xls")
#Rainfall data for every day of the year this year 
df2 = pd.read_csv("C:/Users/eaderman/Downloads/Sydney_Rainfall_Data_2019.csv", usecols = ["Year", "Month", "Day", "Rainfall amount (millimetres)"])

#print(df1.head())
print(df2.head())

df2['Date'] = pd.to_datetime(df2[['Year', 'Month', 'Day']])
ave = float(1000.2/365) #Sydney total for 2018 is 1000.2 mm
ave_weekly = ave*7

# Next 7 days forecast 
ax = df2.iloc[-66:-59].plot(kind='bar', x='Date', y='Rainfall amount (millimetres)', color='b', legend=False) 
#ax.set_xlabel("Date")
plt.axhline(y=ave, color='r', linestyle='dashed', label='Average daily rainfall in Sydney 2018') 
ax.set_ylabel("Rainfall amount (millimetres)")
#ax.set_ylim([-0.05,3.50])
ticklabels = ['']*len(df2.iloc[-66:-59])
ticklabels[::1] = df2['Date'].iloc[-66:-59].dt.strftime('%b %d\n%Y')
ax.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
plt.gcf().autofmt_xdate()
ax.legend() 
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
 
