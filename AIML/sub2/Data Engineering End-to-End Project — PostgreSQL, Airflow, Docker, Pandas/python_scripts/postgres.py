##Load libraries
import psycopg2
import os
import traceback
import logging
import pandas as pd
import urllib.request

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')


# dest_folder = os.environ.get('dest_folder')
# url = "https://raw.githubusercontent.com/dogukannulu/datasets/master/Churn_Modelling.csv"
# destination_path = f'{dest_folder}/churn_modelling.csv'

connection = psycopg2.connect(
        user="Atishay",
        password="sayonee650",
        host="localhost",
        dbname="postgres",
        port="5432"
        # database="AIML_2024"
    )
 

# connection.autocommit = True
# cursor = connection.cursor()
print("Connected to the database")
# Now you can perform operations on the database using the connection

# except (Exception, psycopg2.Error) as error:
#     print(f"Error while connecting to PostgreSQL: {error}")