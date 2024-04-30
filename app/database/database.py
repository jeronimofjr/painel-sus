from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
import pandas as pd
from psycopg2 import OperationalError

def create_conn_and_ingest():
    conn = None
    engine = None
    while not conn:
        try:
            engine = create_engine('postgresql+psycopg2://root:root@db:5432/atendimentos')
            conn = engine.connect()
        except OperationalError as e:
            time.sleep(5)
    
    url = "./data/atendimentos.csv"
    df = pd.read_csv(url, index_col=[0])
    df["data_atendimento"] = pd.to_datetime(df["data_atendimento"], format='mixed')
    df.to_sql(name="atendimentos", con=engine, if_exists='replace', index=False)
    return engine


engine = create_conn_and_ingest()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()



