from flask import Flask, request
import json
from utils import DTRPredict, get_distance_from_redshift

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/predict')
def predict():
    ug = float(request.args.get('ug'))
    gr = float(request.args.get('gr'))
    ri = float(request.args.get('ri'))
    iz = float(request.args.get('iz'))
    # redshift_predicted = DTRPredict(1.89866, 0.947, 0.42289, 0.31376)
    redshift_predicted = DTRPredict(ug, gr, ri, iz)
    distance = get_distance_from_redshift(redshift_predicted)
    result = {
        'redshift': redshift_predicted,
        'distance': distance
    }
    return json.dumps(result, indent=10)


if __name__ == '__main__':
    app.run(debug=True)
