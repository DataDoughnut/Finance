import requests
import datetime as dt
import pandas as pd

polygon_api_key = open("polygon_io_api_key.txt").read()

today = dt.datetime.now().date().strftime("%Y-%m-%d")
future = (dt.datetime.now().date() + dt.timedelta(days=(30))).strftime("%Y-%m-%d")

api_pull = f"https://api.massive.com/benzinga/v1/earnings?sort=last_updated.desc&date.lte={future}&date.gte={today}&apiKey={polygon_api_key}"
api_pull_r = requests.get(api_pull)
api_data = api_pull_r.json()

pd_api = pd.DataFrame(api_data["results"])
pd_api_confirmed = pd_api[pd_api["date_status"] == 'confirmed'].sort_values(by=["date","time"])

earnings_pd = pd_api_confirmed[["importance","company_name", "ticker", "date", "time", "estimated_eps"]]