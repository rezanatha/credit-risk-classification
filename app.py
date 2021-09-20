from flask import Flask, jsonify, json, request
from logging import debug
app = Flask(__name__)
import pickle
from predict import predict_data

preds = []

output = {
    "model":"null",
    "version":"null",
    "score_proba_1":"null"
    }
#format output
# {
#     "model":"german-credit-risk",
#     "version": "1.0.0",
#     "score_proba":{result}
#
# }

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "CREDIT SCORE PREDICTION ;)"



@app.route("/prediction", methods=['POST','GET'])
def make_predictions():
    '''
    Predict input data
    '''
    if request.method == "GET":
        return jsonify(output)
    if request.method == "POST":
        data = request.get_json()
        result = predict_data(data)
        print(result)
        proba_1 = float(result[:, 1])
        output["model"] = "credit-risk"
        output["version"] = "1.0.0"
        output["score_proba_1"] = proba_1
        return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
