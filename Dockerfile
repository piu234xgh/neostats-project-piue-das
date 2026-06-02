# =========================
# BASE IMAGE
# =========================

FROM python:3.11

# =========================
# WORK DIRECTORY
# =========================

WORKDIR /app

# =========================
# COPY FILES
# =========================

COPY . .

# =========================
# INSTALL REQUIREMENTS
# =========================

RUN pip install --no-cache-dir -r requirements.txt

# =========================
# EXPOSE STREAMLIT PORT
# =========================

EXPOSE 8501

# =========================
# RUN STREAMLIT
# =========================

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
