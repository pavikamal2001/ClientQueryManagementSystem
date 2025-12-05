import streamlit as st
import psycopg2
import hashlib

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



st.markdown("""
<h1 style="text-align:center; color:#1A73E8;">
WELCOME TO SUPPORT QUERY PORTAL
</h1>
""", unsafe_allow_html=True)

# Inputs
username = st.text_input("Enter your Name")
password = st.text_input("Enter your Password", type='password')
role = st.selectbox("Select roles", ["client", "support"])

if st.button("Login"):

    
    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="clientdb",
            user="postgres",
            password="Pavikamal29",
            port="5432"
        )
        cur = conn.cursor()

        # Step 3: Fetch stored hashed password
        cur.execute("SELECT hashed_password FROM users WHERE username=%s AND roles=%s", (username, role))
        result = cur.fetchone()

        if result:
            stored_hash = result[0]
            # st.write("DEBUG values:")
            # st.write("Entered Hash:", hash_pass)
            # st.write("Stored hash:", stored_hash)

            
            if hash_pass == stored_hash:
                st.success("Login Successful!")

                
                if role == "client":
                    st.switch_page("Pages/client.py")
                elif role == "support":
                    st.switch_page("pages/query.py")

            else:
                st.error("Incorrect password")
        else:
            st.error("User does not exist")

    except Exception as e:
        st.error(f"Database error: {e}")

       