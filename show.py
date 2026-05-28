import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Dev12345@database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com:5432/studentdb"
)

df = pd.read_sql("SELECT * FROM students", engine)

print(df)