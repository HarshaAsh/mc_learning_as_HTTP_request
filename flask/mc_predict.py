# import dill
import requests
import pandas as pd
import numpy as np
from math import sqrt
import datetime
from dateutil.relativedelta import relativedelta
def predict(date):
    with open('/home/harshaash/mysite/predict_hyderabad_pm25.pkl', "rb") as pkl_file:
        model = dill.load(pkl_file)
    return model.predict(date)
#     try:
#         # Getting the actual and predictions of the last two days for ARIMA(2,0,2)
#         date = (datetime.datetime.strptime(date, "%Y-%m-%d")- relativedelta(days=4)).strftime("%Y-%m-%d")
#         response = requests.get("https://hydpm25.herokuapp.com/get_last_n_days_data", params={'date': date, 'n':4})
#         df = pd.DataFrame(response.json()['result'])[-2:]
#         df['ma'] = df.actual - df.predicted
#         df['ma_slope'] = [-0.7915, -0.0775]
#         df['ar_slope'] = [1.5876, -0.5914]
#         pred = 0.4454+sum(df.ma*df.ma_slope+df.actual*df.ar_slope) + abs(np.random.normal(0, sqrt(200.55), 1))
#         return pred
#     except:
#         return [115.6]
