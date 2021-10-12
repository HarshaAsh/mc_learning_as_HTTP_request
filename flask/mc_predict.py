import dill
def predict(df):
    with open('predict_hyderabad_pm25.pkl', "rb") as pkl_file:
        model = dill.load(pkl_file)
    return model.predict(df)

# Location would be /home/harshaash/mysite/predict_hyderabad_pm25.pkl