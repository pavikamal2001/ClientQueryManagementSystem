import streamlit as st
import pandas as pd
from datetime import datetime
import psycopg2

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

st.markdown("<h1 style='text-align:center; color:#1A73E8; margin-bottom:0;'>Support Team - Query Management</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; margin-top:0;'>Client Query Portal</h2>", unsafe_allow_html=True)




# -------- PostgreSQL Connection --------
def get_connection():
    return psycopg2.connect(
        host="localhost",
            database="clientdb",
            user="postgres",
            password="Pavikamal29",
            port="5432"
    )

# -------- Load PostgreSQL Data --------
def load_queries_db():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM queries ORDER BY query_id ASC", conn)
    conn.close()
    return df

# -------- Load OLD CSV History --------
def load_csv_history():
    df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/streamlit/Pages/synthetic.csv")

    # Rename CSV columns → match DB structure
    df = df.rename(columns={
        "client_email": "email",
        "client_mobile": "mobile",
        "query_heading": "category",
        "query_description": "query_description",
        "date_raised": "query_created_time",
        "date_closed": "query_closed_time"
    })

    # Ensure query_id is string
    df["query_id"] = df["query_id"].astype(str)

    return df

# -------- Streamlit App --------



# Load CSV History
st.markdown("<h3 style='text-align:left; color:#c0392b;'> CSV History Data:</h3>", unsafe_allow_html=True)


df_csv = load_csv_history()
st.dataframe(df_csv)

# Load Live DB Records
st.markdown("<h3 style='text-align:left; color:#c0392b;'> Load Live DB Records:</h3>", unsafe_allow_html=True)
df_db = load_queries_db()
st.dataframe(df_db)

st.markdown("<h3 style='text-align:left; color:#c0392b;'> Close a Query:</h3>", unsafe_allow_html=True)

if not df_db.empty:
    open_db_queries = df_db[df_db["status"] == "Open"]

    if open_db_queries.empty:
        st.info("No open queries in database.")
    else:
        selected_query = st.selectbox(
            "Select Query ID to Close",
            open_db_queries["query_id"].tolist()
        )

        if st.button("Close Selected Query"):
            try:
                conn = get_connection()
                cur = conn.cursor()

                update_sql = """
                    UPDATE queries
                    SET status = %s,
                        query_closed_time = %s
                    WHERE query_id = %s
                """

                cur.execute(update_sql, ("Closed", datetime.now(), selected_query))
                conn.commit()
                cur.close()
                conn.close()

                st.success(f"Query ID {selected_query} closed successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error updating query: {e}")


# step 10 LOGOUT BUTTON 
if st.button("Log out"):
    st.switch_page("client.py")