

import psycopg2
import sys as die	
#from .logs import die
import mariadb
import pandas as pn

#import matplotlib.pyplot as plt
from sqlalchemy import create_engine

import sqlalchemy as sql

#engine = create_engine("mariadb:///?User=root&;Password=yeshey010&Database=esakor&Server=localhost&Port=3306")
con = mariadb.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "yeshey010",
    database = "esakor" 
  )
df = pn.read_sql("select * from Thram where cthram=3321 and cgewog=29", con)

print(df)


uri = psycopg2.connect(
    host = "localhost",
    port = 5432,
    user = "postgres",
    password = "yeshey010",
    database = "esakor1" 
  )


def insert_data(self, df: pn.DataFrame, schema: str, table: str, chunksize: int=100) -> None:
        """This function abstracts the `INSERT` queries

        Args:
            df (pn.DataFrame): dataframe to be inserted
            schema (str): the name of the schema
            table (str): the name of the table
            chunksize (int): the number of rows to insert at the time
        """
        try:
            engine = sql.create_engine(self.uri)
            with engine.connect() as uri:
                tran = uri.begin()
                df.to_sql(
                    name=table, schema=schema,
                    con=uri, if_exists="append", index=False,
                    chunksize=chunksize, method="multi"
                )
                tran.commit()
        except Exception as e:
            if 'tran' in locals():
                tran.rollback()
            die(f"{e}")

