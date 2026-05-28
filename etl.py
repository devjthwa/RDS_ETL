import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv("students.csv", encoding="utf-8-sig")

# 🔄 Transform (THIS is what was missing)

# 1. Clean column names
df.columns = df.columns.str.strip()

# 2. Remove nulls
df = df.dropna()

# 3. Create new column (if not already meaningful)
df["Average Marks"] = df[["Mathematics", "Science", "English", "History"]].mean(axis=1)

# 4. Grade system
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

df["Grade"] = df["Average Marks"].apply(grade)

# 5. Normalize names
df["Student Name"] = df["Student Name"].str.title()

# Load
engine = create_engine(
    "postgresql+psycopg2://postgres:Dev12345@database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com:5432/studentdb"
)

df.to_sql("students", engine, if_exists="replace", index=False)

print("ETL completed with transformations")