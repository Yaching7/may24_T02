def format_model_input (input_dict):
        tenure_months = int(input_dict['tenure_months'])
        total_monthly_fee = float(input_dict['total_monthly_fee'])
        age = int(input_dict['age'])
        num_dependents = int(input_dict['num_dependents'])
        contract_type = int(input_dict['contract_type'])
        payment_method = int(input_dict['payment_method'])
        married = int(input_dict['married'])
        zip_code = int(input_dict['zip_code'])
        num_referrals = int(input_dict['num_referrals'])

    return [tenure_months, total_monthly_fee, age, num_dependents, contract_type, payment_method, married, zip_code, num_referrals]