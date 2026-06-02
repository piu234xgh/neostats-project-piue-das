import streamlit as st
import pandas as pd
import joblib

from src.talk_to_data.nl_to_sql import (
    generate_sql,
    explain_result
)

from src.talk_to_data.query_runner import (
    run_query
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Credit Risk Platform",
    layout="wide"
)

st.title("AI Credit Risk Platform")

# =========================
# SIDEBAR
# =========================

page = st.sidebar.selectbox(

    "Select Module",

    [
        "ML Prediction",
        "Talk To Data Chatbot"
    ]

)

# =========================
# LOAD MODEL
# =========================

model = joblib.load("model.pkl")

# =========================
# ML PREDICTION PAGE
# =========================

if page == "ML Prediction":

    st.header("Loan Default Prediction")

    # INPUTS

    gender = st.selectbox(
        "Gender",
        ["M", "F"]
    )

    income = st.number_input(
        "Total Income",
        value=150000
    )

    credit = st.number_input(
        "Credit Amount",
        value=500000
    )

    annuity = st.number_input(
        "Annuity Amount",
        value=25000
    )

    days_birth = st.number_input(
        "Days Birth",
        value=-12000
    )

    days_employed = st.number_input(
        "Days Employed",
        value=-3000
    )

    children = st.number_input(
        "Children Count",
        value=1
    )

    education = st.selectbox(

        "Education",

        [
            "Higher education",
            "Secondary / secondary special",
            "Incomplete higher",
            "Lower secondary",
            "Academic degree"
        ]

    )

    family = st.selectbox(

        "Family Status",

        [
            "Married",
            "Single / not married",
            "Civil marriage",
            "Separated",
            "Widow"
        ]

    )

    # =========================
    # PREDICT BUTTON
    # =========================

    if st.button("Predict Risk"):

        # ENCODING

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

        # CREATE DATAFRAME

        input_df = pd.DataFrame([{

            "CODE_GENDER":
                gender_map[gender],

            "AMT_INCOME_TOTAL":
                income,

            "AMT_CREDIT":
                credit,

            "AMT_ANNUITY":
                annuity,

            "DAYS_BIRTH":
                days_birth,

            "DAYS_EMPLOYED":
                days_employed,

            "CNT_CHILDREN":
                children,

            "NAME_EDUCATION_TYPE":
                education_map[education],

            "NAME_FAMILY_STATUS":
                family_map[family]

        }])

        # PREDICT

        prediction = model.predict(input_df)

        prediction_proba = (
            model.predict_proba(input_df)
        )

        risk_score = (
            prediction_proba[0][1] * 100
        )

        # RISK BAND

        if risk_score < 30:

            risk_band = "LOW"

        elif risk_score < 70:

            risk_band = "MEDIUM"

        else:

            risk_band = "HIGH"

        # OUTPUT

        st.success(
            f"Risk Score: {risk_score:.2f}%"
        )

        st.warning(
            f"Risk Band: {risk_band}"
        )

# =========================
# CHATBOT PAGE
# =========================

elif page == "Talk To Data Chatbot":

    st.header("SQL AI Chatbot")

    question = st.text_input(
        "Ask Question"
    )

    if st.button("Ask AI"):

        sql_query = generate_sql(question)

        st.subheader("Generated SQL")

        st.code(sql_query)

        try:

            result = run_query(sql_query)

            st.subheader("Query Result")

            st.dataframe(result)

            explanation = explain_result(
                question,
                result
            )

            st.subheader("AI Explanation")

            st.write(explanation)

        except Exception as e:

            st.error(str(e))