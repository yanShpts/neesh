import pandas as pd 
from pytrends.request import TrendReq
from datetime import date

pytrends = TrendReq(hl='en-US', tz=360)

trends = pytrends.trending_searches(pn='united_states')

topItem = trends[0].iloc[0]

kw_list = ['food near me', "new years"] #the keyword to get results for 
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='') #builds payload for keyword and interest over last 12 months

print(trends[0].iloc[0])