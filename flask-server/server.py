from flask import Flask, request
import pandas as pd
import jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

#check file directory for a .csv, if there isn't one then make one to store entries and scores
df = pd.DataFrame(columns=['interest','score'])

#pytrends API Route
@app.route("/pytrends", methods=['POST'])
def trend_data():
    pytrends = TrendReq(hl='en-US', tz=360)
    #get user input
    kw_list = request.get_json()

    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')#builds payload for keyword and interest over last 12 months
    data = pytrends.interest_over_time() #returns pandas.DataFrame
    #adds column to store the interest being tracked
    data['interest'] = kw_list[0]
    # Renaming the columns to match the sentiment DataFrame
    data = data.rename(columns={"score": "score", "date": "date"})
    # Dropping the 'isPartial' column
    data.drop(columns=["isPartial"], inplace=True)
    
    #add the current row to the DataFrame
    global df
    df = pd.concat([df,data], ignore_index=True)

    niche_score = data['score'].sum() #sums all values in the 'score' column
    return jsonify(data.to_dict())


@app.route("/get_last_5")
def get_last_5():
    global df
    last_5_entries = df.tail(5)
    last_5_entries_trimmed = last_5_entries[['interest', 'score']].to_dict(orient='records')
    return last_5_entries_trimmed

if __name__ == "__main__":
    app.run(debug=True, port=5000)