import joblib
from os import system

# uninitialized model
model = None


def load_model() -> None:
    global model

    model = joblib.load('model/loan-pred.pkl')


if __name__ == '__main__':
    print('loading model... please wait π')
    load_model()
    system('cls')

    print('Loan Eligibility ->>>>>> π²\n')
    gender = int(input('Enter gender π¬ ->>> for MALE(1) and FEMALE(0): '))
    married = int(input('Enter your martial π° status ->>> YES(1) and NO(0): '))
    dependents = int(input('Enter how many dependentsπΆ?: '))
    education = int(input('Graduated or not π? YES(1) and NO(0): '))
    self_education = int(input('Self-Employed or not π’? YES(1) and NO(0): '))
    applicant_income = float(input('Enter applicants income πΈ: '))
    coapplicant_income = float(input('Enter co-applicant income π°: '))
    loan_amount = float(input('Enter your loan in dollars π²: '))
    loan_amount_term = float(input('Enter loan amount term πΉ: '))
    credit_history = int(
        input('Enter your credit history π³->>> YES(1) and NO(0): '))
    property_area = int(
        input('Enter your property area π  ->>> RURAL(0), SEMI-URBAN(1) and URBAN(2): '))

    predicted_value = model.predict([[gender, married, dependents, education, self_education,
                                    applicant_income, coapplicant_income, loan_amount,loan_amount_term, credit_history, property_area]])

    if(predicted_value[0]):
        print('You are eligible for this loan π')
    else:
        print('Sorry... you are not eligible for this loan π')
