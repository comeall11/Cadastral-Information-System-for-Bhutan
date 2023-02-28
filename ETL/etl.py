# ETL Part for tranfering data from other datasources(in our case Mariadb database) to our working PostgresSQL database
# Requirements
import psycopg2
import sys as die
import mariadb
import pandas as pn
from sqlalchemy import create_engine
import sqlalchemy as sql

# Database Connect with Maridb database and postgressql and reading the data to migrate from mariadb to postgressql
con = mariadb.connect(
    host="localhost",
    port=3306,
    user="root",
    password="yeshey010",
    database="esakor"
)
district = pn.read_sql("select * from district", con)
block = pn.read_sql("select * from district", con)
thram = pn.read_sql("select * from district", con)
owntype = pn.read_sql("select * from district", con)
landtype = pn.read_sql("select * from district", con)
plot = pn.read_sql("select * from district", con)

uri = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="yeshey010",
    database="esakor1"
)

# Function to insert the data tables(district,block,thram,plot,owntype,landtype) to the schema in the postgressql


def insert_data(self, district: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=district, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")


def insert_data(self, block: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=block, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")


def insert_data(self, thram: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=thram, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")


def insert_data(self, owntype: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=owntype, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")


def insert_data(self, landtype: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=landtype, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")


def insert_data(self, plot: pn.DataFrame, schema: str, table: str, chunksize: int = 100) -> None:
    try:
        engine = sql.create_engine(self.uri)
        with engine.connect() as uri:
            tran = uri.begin()
            district.to_sql(
                name=plot, schema=schema,
                con=uri, if_exists="append", index=False,
                chunksize=chunksize, method="multi"
            )
            tran.commit()
    except Exception as e:
        if 'tran' in locals():
            tran.rollback()
        die(f"{e}")
