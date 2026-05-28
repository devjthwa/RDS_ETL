import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Dev12345@database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com:5432/studentdb"
)

df = pd.read_sql("SELECT * FROM students", engine)

st.title("Student Dashboard")

st.dataframe(df)

st.subheader("Summary")

st.write("Total Students:", len(df))
st.write("Average Percentage:", df["Percentage"].mean())
st.write("Top Score:", df["Percentage"].max())