from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine

app = FastAPI()

# DB connection (same as your ETL)
engine = create_engine(
    "postgresql+psycopg2://postgres:Dev12345@database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com:5432/studentdb"
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/students")
def get_students():
    df = pd.read_sql("SELECT * FROM students", engine)
    return df.to_dict(orient="records")

@app.get("/top-students")
def top_students():
    df = pd.read_sql("SELECT * FROM students ORDER BY \"Percentage\" DESC LIMIT 5", engine)
    return df.to_dict(orient="records")


@app.get("/students/grade/{grade}")
def students_by_grade(grade: str):
    query = f'SELECT * FROM students WHERE "Grade" = \'{grade}\''
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

@app.get("/summary")
def summary():
    df = pd.read_sql("SELECT * FROM students", engine)

    return {
        "total_students": len(df),
        "average_percentage": float(df["Percentage"].mean()),
        "top_percentage": float(df["Percentage"].max())
    }
