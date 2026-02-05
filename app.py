import streamlit as st
import sqlite3
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ USE GEMINI 2.5 FLASH
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

st.title("🧠 SQL LLM Application")
st.write("Ask questions in English. The AI will convert them into SQL and fetch results.")

question = st.text_input("Enter your question")

def run_sql(sql_query):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.close()
    return result

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        prompt = f"""
Convert the following English question into an SQL query.

Table name: students
Columns:
- id
- name
- marks

Question: {question}

Return ONLY the SQL query. No explanation.
"""

        try:
            response = model.generate_content(prompt)
            sql_query = response.text.strip()

            st.subheader("Generated SQL")
            st.code(sql_query, language="sql")

            data = run_sql(sql_query)

            st.subheader("Result")
            st.write(data)

        except Exception as e:
            st.error(f"Error: {e}")