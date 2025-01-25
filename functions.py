import pandas as pd
import tomllib
import psycopg2

def load_db_credentials(config_file):
    with open(config_file, "rb") as f:
        config = tomllib.load(f)
    return config


def connect_to_database(credentials_file):
    credentials = load_db_credentials(credentials_file)  # Path to your TOML file
    connection = psycopg2.connect(
        dbname=credentials["dbname"],
        user=credentials["user"],
        password=credentials["password"],
        host=credentials["host"],
        port=credentials["port"]
    )
    return connection


def get_table_names(cursor):
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
    """)

    # Fetch all results
    tables = cursor.fetchall()
    return [x[0] for x in tables]



def table_name_to_df(cursor, table_name:str, page_number=1):
    
    page_size = 100
    
    offset = (page_number - 1) * page_size
    
    query = f"SELECT * FROM {table_name} LIMIT {page_size} OFFSET {offset};"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    
    return pd.DataFrame(columns=column_names, data=rows)