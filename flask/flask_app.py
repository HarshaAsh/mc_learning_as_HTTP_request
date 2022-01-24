from flask import Flask, request, jsonify, render_template
import dill
import requests
import pandas as pd
import numpy as np
from math import sqrt
import datetime
from dateutil.relativedelta import relativedelta
from mc_predict import predict as machine_learning_predict

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def base_website():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_request():
    query_date = request.args.get('date', default='2021-11-08', type = str)
    prediction = machine_learning_predict(query_date)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    # mc_train.main()
    app.run(debug=True)
