from flask import Flask, request, jsonify
import pandas as pd
from mc_predict import predict as machine_learning_predict

app = Flask(__name__)


@app.route("/")
def base_website():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['GET'])
def predict_request():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    prediction = machine_learning_predict(query_df)
    return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
    # mc_train.main()
    app.run(debug=True)