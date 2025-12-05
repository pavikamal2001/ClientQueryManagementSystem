import streamlit as st
import psycopg2
from datetime import datetime



def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="clientdb",
        user="postgres",
        password="Pavikamal29",
        
    )
st.markdown(
    """
    <h1 style="text-align:center; font-family:'Georgia'; color:#c0392b;">
        Report Issues
    </h1>
    <h3 style="text-align:center; color:#1A73E8;">
        Raise Your Quality or Delivery Complaints Here.
    </h3>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://img.freepik.com/free-photo/dark-gray-concrete-wall_53876-63609.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    
    unsafe_allow_html=True
)
mail_id = st.text_input("Email ID")
mobile_number = st.text_input("Mobile number")
query_heading= st.text_input("query_heading")
description = st.text_area("Query Description")


if st.button("Submit"):
     if not mail_id or not mobile_number or query_heading == "" or not description:
        st.warning("Please fill in all the fields before submitting!")

     else: 
        conn = get_connection()
        cur = conn.cursor()
        insert_sql="""INSERT INTO queries(mail_id,mobile_number,query_heading,query_description,status,query_created_time,query_closed_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""

        cur.execute(insert_sql,(
            mail_id,mobile_number,query_heading,description,"Open",datetime.now(),None
        ))
        conn.commit()
        cur.close()
        conn.close()
        st.success("Query Submitted Successfully")
      
if st.button("Log out"):
    st.switch_page("pavi.py")