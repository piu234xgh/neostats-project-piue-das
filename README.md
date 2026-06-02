
# Credit Risk NL to SQL Chatbot

## Features
1. Load all CSV files from data folder
2. Convert CSV files into SQLite database
3. Convert Natural Language to SQL using Gemini
4. Run SQL query on SQLite DB
5. Return results to user

---

## Project Structure

credit_risk_platform/
│
├── data/
│   └── put all csv files here
│
├── src/
│   └── talk_to_data/
│       ├── create_db.py
│       ├── nl_to_sql.py
│       ├── query_runner.py
│       └── chatbot.py
│
├── credit.db
├── requirements.txt
└── .env.example

---

## Step 1: Install Requirements

pip install -r requirements.txt

---

## Step 2: Add CSV Files

Put all kaggle CSV files inside:

data/

---

## Step 3: Create SQLite Database

Run:

python -m src.talk_to_data.create_db

This creates:
credit.db

---

## Step 4: Add Gemini API Key

Rename:

.env.example → .env

Add your API key.

---

## Step 5: Run Chatbot

Run:

python -m src.talk_to_data.chatbot

---

## Example Questions

Which gender has highest defaults?

Average income of defaulters?

Which education type is riskiest?

Show top 5 highest credit amounts

---

## Exit Chatbot

Type:

exit
