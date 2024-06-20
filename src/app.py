from flask import Flask, request, render_template
from model import Model
from input_processing import format_model_input

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
       
        model_inputs = format_model_input(form_input)
        prediction = Model().predict(model_inputs)

        if prediction == 1:
            prediction_label = "The customer will churn"

        else:
            prediction_label = "The customer will stay"

        return render_template('index.html', prediction=prediction_label)

    return render_template('index.html')


# Method 2: Via POST API
def predict():
    request_data = request.get_json()

    # Added code in orange
    age = int(request_data['age'])
    sex = request_data['sex']
    bmi = float(request_data['bmi'])
    children = int(request_data['children'])
    smoker = request_data['smoker']
    region = request_data['region']

    model_inputs = [age, sex, bmi, children, smoker, region]
    prediction = Model().predict(model_inputs)

    return {'prediction': prediction}


if __name__ == '__main__':
    app.run(debug=True)
