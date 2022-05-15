from flask import Flask, request

# method to load model from file
def load_model() -> None:
    global model
    import joblib

    model = joblib.load('model/loan-pred.pkl')
    

api = Flask(__name__)

model = None

@api.route('/predict',methods=['POST'])
def predict_loan_status():
    data = request.json

    return data

with api.app_context():
    load_model()


if __name__ == '__main__':
    api.run(debug=True)