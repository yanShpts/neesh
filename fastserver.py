from fastapi import FastAPI, Request
import uvicorn
import pandas as pd 
from pytrends.request import TrendReq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This middleware is required in order to accept requests from other domains such as a React app running on 'localhost:3000'
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return({ "message": "hello world" })

df = pd.DataFrame(columns=['interest', 'score'])



# PyTrends API Route
@app.post("/pytrends")
def trend_data(request: Request):
    pytrends = TrendReq(hl='en-US', tz=360)
    # Get user input as a list
    kw_list = request.json()['text']#gets JSON and extracts the input keyword
    

    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')  # Builds payload for keyword and interest over the last 12 months
    data = pytrends.interest_over_time()  # Returns pandas.DataFrame

    # Calculate the niche score by summing the 'score' column
    niche_score = data[kw_list[0]].sum()

    # Create a dictionary with the interest and score
    data_dict = {"interest": kw_list[0], "score": niche_score}

    # Add the current row to the DataFrame
    global df
    df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)

    return {"score": niche_score}


@app.get("/get_last_5")
def get_last_5():
    global df

    last_5_entries = df.tail(5)
    last_5_entries_trimmed = last_5_entries[['interest', 'score']].to_dict(orient='records')
    return last_5_entries_trimmed



if __name__ == "__main__":
    uvicorn.run("fastserver:app", port=5000, reload=True)
