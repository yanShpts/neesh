import pandas as pd 
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain"] #the keyword to get results for 
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')#builds payload for keyword and interest over last 12 months

print(pytrends.interest_over_time())