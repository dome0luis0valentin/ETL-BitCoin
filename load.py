# import sqlite3 
import psycopg2
import csv

import pandas as pd
from sqlalchemy import create_engine
"""
Load the data of back stage
"""

def insert_data(cursor, connection):
    path_source = "./target/Precio_Bitcoin_ARS.csv"
    with open(path_source, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            name, price_ars = row
            insert_query = "INSERT INTO bitcoin (name, price_ars) VALUES (%s, %s);"
            cursor.execute(insert_query, (name, float(price_ars)))

    connection.commit()

def load():
    """
    Take the data of csv and load in a DB
    """
    name_db = "Bitcoin"

    
    db_params = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'postgres',
    }
    
    name_table = "Bitcoin"
    path_source = "./target/Precio_Bitcoin_ARS.csv"


    # connection = sqlite3.connect(name_db)
    conn = psycopg2.connect(**db_params, database='postgres')
    
    conn.autocommit = True
    cursor = conn.cursor()    
    
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {name_table}  (
        id serial PRIMARY KEY,
        name VARCHAR (100) NOT NULL,
        age INT
    );
    '''

    cursor.execute(create_table_query)
    
    
    conn.commit()
        
    df = pd.read_csv(path_source) 

    # Create a SQLAlchemy engine
    engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/postgres')

        # Write DataFrame to PostgreSQL database
    df.to_sql('bitcoin', engine, if_exists='replace', index=False)


    
       
    # Use pandas to write the DataFrame to the PostgreSQL database
    # engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{name_db}')
    # df.to_sql(name_table, engine, index=False, if_exists='replace')
    cursor.close()
    conn.close()
        