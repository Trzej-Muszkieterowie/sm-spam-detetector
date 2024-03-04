from model import Model
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model = Model()
    model.load_data()
    model.train()
    return jsonify(model.predict(data['texts']).tolist())

if __name__ == '__main__':
    app.run(debug=False)