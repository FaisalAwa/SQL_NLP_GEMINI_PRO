# from dotenv import load_dotenv
# load_dotenv()  # Load all the environment variables

# import streamlit as st
# import os
# import sqlite3

# import google.generativeai as genai

# # Configure our API KEY
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to load Google Gemini Model and provide SQL query as response
# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content([prompt[0], question])
#     return response.text.strip()

# # Function to retrieve query from the SQL database
# def read_sql_ready(sql, db):
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     return rows

# # Define your prompt
# prompt = [
#     r"""
#     You are an expert in converting English queries to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS.
#     For example, \nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
#     \nExample 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
#     Also, the SQL code should not have ``` in beginning or end and the word sql should not be in the output.
#     """
# ]

# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")
# question = st.text_input("Input:", key="input")
# submit = st.button("Ask the question")

# # if submit is clicked
# if submit:
#     response = get_gemini_response(question, prompt)
#     st.subheader("Generated SQL Query:")
#     st.code(response, language='sql')
    
#     data = read_sql_ready(response, "student.db")
#     st.subheader("The Response is:")
#     for row in data:
#         st.write(row)




from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure our API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve query from the SQL database
def read_sql_ready(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define your prompt
prompt = [
    r"""
    You are an expert in converting English queries to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS.
    For example, \nExample 1 - How many entries of records are present?, the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    Also, the SQL code should not have ``` in beginning or end and the word sql should not be in the output.
    """
]

# Custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FF5733;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #33FF57;
        }
        .description {
            font-size: 18px;
            color: #FFFFFF;
        }
        .stTextInput > div > input {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        .stButton > button {
            background-color: #FF5733;
            color: #FFFFFF;
        }
        .stCodeBlock > div {
            background-color: #001f3f;
            color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# SVG Animation for SQL Query Generator
st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <g>
    <title>SQL Query Generator</title>
    <rect width="100%" height="200" fill="#001f3f" />
    <rect x="10%" y="20" width="80%" height="160" fill="#33FF57" />
    <text x="50%" y="100" font-size="24" font-family="Arial" fill="#FF5733" text-anchor="middle">
      <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
      📊 SQL Query Generator 🔍
    </text>
  </g>
</svg>
""", unsafe_allow_html=True)

# Streamlit app
# st.set_page_config(page_title="I can Retrieve Any SQL query")
st.markdown('<div class="header">📊 Gemini App To Retrieve SQL Data 🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Convert Natural Language to SQL and Display Results!</div>', unsafe_allow_html=True)

# Project description
st.markdown("""
### Project Description:
Welcome to the Gemini App! This tool is designed to help you convert natural language queries into SQL commands and retrieve data from your SQL database. By leveraging the power of Google Gemini, this app allows you to simply input a question in plain English, and it will generate the corresponding SQL query. This is particularly useful for users who are not familiar with SQL syntax but need to query a database. Upload your database, ask your question, and get your data instantly!
""")

question = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.code(response, language='sql')
    
    data = read_sql_ready(response, "student.db")
    st.subheader("The Response is:")
    for row in data:
        st.write(row)
