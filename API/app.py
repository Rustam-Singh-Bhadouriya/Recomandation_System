import helper
from flask import Flask, jsonify, request
import tensorflow as tf
import pandas as pd
import numpy as np

import helper.formatter

model = tf.keras.models.load_model("Model/Recormandation_System.keras")

app = Flask(__name__)

@app.route("/")
def hey():
    return "<h1>Recomandation System API</h1>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=False)

    features = data['features']

    if len(features) != 12:
        return jsonify({"error": "Model expects 12 features"}), 400
    

    formatted_data = helper.formatter.Simplify_split_arr(np.array(features, dtype=object))

    prediction = model.predict(formatted_data)
    prediction = helper.formatter.Simplify_pred(predictions=prediction)
    return jsonify({
        "prediction": prediction.tolist()
    })


    

if __name__ == "__main__":
    app.run(debug=True)