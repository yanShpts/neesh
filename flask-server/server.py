from flask import Flask
import pandas as pd
import jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

#pytrends API Route
@app.route("/pytrends")
def trend_data():
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Blockchain"] #should take in user input
    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')#builds payload for keyword and interest over last 12 months
    data = pytrends.interest_over_time()

    return jsonify(data.to_dict())

if __name__ == "__main__":
    app.run(debug=True)