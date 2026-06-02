import joblib
import pandas as pd

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model.pkl")

print("Model Loaded Successfully")

# =========================
# USER INPUT
# =========================

input_data = {

    "CODE_GENDER": "M",

    "AMT_INCOME_TOTAL": 150000,

    "AMT_CREDIT": 500000,

    "AMT_ANNUITY": 25000,

    "DAYS_BIRTH": -12000,

    "DAYS_EMPLOYED": -3000,

    "CNT_CHILDREN": 1,

    "NAME_EDUCATION_TYPE": "Higher education",

    "NAME_FAMILY_STATUS": "Married"

}

# =========================
# CONVERT TO DATAFRAME
# =========================

df = pd.DataFrame([input_data])

# =========================
# MANUAL ENCODING
# =========================

gender_map = {

    "M": 0,
    "F": 1

}

education_map = {

    "Higher education": 0,
    "Secondary / secondary special": 1,
    "Incomplete higher": 2,
    "Lower secondary": 3,
    "Academic degree": 4

}

family_map = {

    "Married": 0,
    "Single / not married": 1,
    "Civil marriage": 2,
    "Separated": 3,
    "Widow": 4

}

df["CODE_GENDER"] = df["CODE_GENDER"].map(gender_map)

df["NAME_EDUCATION_TYPE"] = (
    df["NAME_EDUCATION_TYPE"]
    .map(education_map)
)

df["NAME_FAMILY_STATUS"] = (
    df["NAME_FAMILY_STATUS"]
    .map(family_map)
)

# =========================
# PREDICTION
# =========================

prediction = model.predict(df)

prediction_proba = model.predict_proba(df)

risk_score = prediction_proba[0][1] * 100

# =========================
# RISK BAND
# =========================

if risk_score < 30:

    risk_band = "LOW"

elif risk_score < 70:

    risk_band = "MEDIUM"

else:

    risk_band = "HIGH"

# =========================
# OUTPUT
# =========================

print("\nPrediction:", prediction[0])

print(f"Risk Score: {risk_score:.2f}%")

print("Risk Band:", risk_band)