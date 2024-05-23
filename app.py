from flask import Flask, request, render_template
import joblib
import numpy as np

model = joblib.load('heart_disease_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [float(x) for x in request.form.values()]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = prediction[0]
        
        if output == 1:
            prediction_text = 'Person have heart disease'
            prediction_color = 'positive'
        else:
            prediction_text = 'Person does not have heart disease'
            prediction_color = 'negative'
        
        return render_template('index.html', prediction_text=prediction_text, prediction_color=prediction_color)

if __name__ == "__main__":
    app.run(debug=True)
