import psycopg2
import streamlit as st

from functions import connect_to_database
from functions import get_table_names, table_name_to_df


# Database operations
connection = connect_to_database(credentials_file="local.toml")
cursor = connection.cursor()
table_names = get_table_names(cursor)


# Layout

st.title('GlanceDB')
if st.button('Reload'):
    st.rerun()

tabs = st.tabs(table_names)

for i, table_name in enumerate(table_names):
    tabs[i].dataframe(table_name_to_df(cursor, table_name, page_number=1))

cursor.close()

