import pandas as pd 
import pytrends

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["Blockchain"] #the keyword to get results for 
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')