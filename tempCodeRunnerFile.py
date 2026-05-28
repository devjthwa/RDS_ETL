import pandas as pd
from sqlalchemy import create_engine

def run_etl():
    df = pd.read_csv("students.csv", encoding="utf-8-sig")

    df.columns = df.columns.str.strip()

    df["Average Marks"] = df[["Mathematics", "Science", "English", "History"]].mean(axis=1)

    def grade(m):
        if m >= 90:
            return "A+"
        elif m >= 75:
            return "A"
        elif m >= 60:
            return "B"
        else:
            return "C"

    df["Grade"] = df["Average Marks"].apply(grade)

    engine = create_engine(
        "postgresql+psycopg2://postgres:Dev12345@database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com:5432/studentdb"
    )

    df.to_sql("students", engine, if_exists="replace", index=False)

    print("ETL completed successfully")

if __name__ == "__main__":
    run_etl()