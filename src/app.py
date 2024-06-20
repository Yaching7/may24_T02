from flask import Flask, request, render_template
from model import Model

app = Flask(__name__)


# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)
        tenure_months = int(form_input['tenure_months'])
        total_monthly_fee = float(form_input['total_monthly_fee'])
        age = int(form_input['age'])
        num_dependents = int(form_input['num_dependents'])
        contract_type = int(form_input['contract_type'])
        payment_method = int(form_input['payment_method'])
        married = int(form_input['married'])
        zip_code = int(form_input['zip_code'])
        num_referrals = int(form_input['num_referrals'])


        model_inputs = [tenure_months, total_monthly_fee, age, num_dependents, contract_type, payment_method, married, zip_code, num_referrals]
        prediction = Model().predict(model_inputs)
        return render_template('index.html', prediction=prediction)

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
