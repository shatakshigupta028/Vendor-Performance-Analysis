import pandas as pd
import os
import logging
import time
from sqlalchemy import create_engine

# logging setup
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# DB connection
engine = create_engine('sqlite:///inventory.db')

def ingest_db(file_path, table_name, engine):
    '''ingest CSV into DB using chunks'''
    
    chunk_size = 50000  

    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
        if i == 0:
            chunk.to_sql(table_name, con=engine, if_exists='replace', index=False)
        else:
            chunk.to_sql(table_name, con=engine, if_exists='append', index=False)

        logging.info(f"{table_name}: Inserted chunk {i+1}")

def load_raw_data():
    '''load CSVs and ingest into DB'''
    
    start = time.time()

    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            table_name = file[:-4]

            logging.info(f"Starting ingestion for {file}")
            ingest_db(file_path, table_name, engine)

    end = time.time()
    total_time = (end - start) / 60

    logging.info('-----------Ingestion Complete------------')
    logging.info(f'Total time taken: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()