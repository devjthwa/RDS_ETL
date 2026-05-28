import psycopg2

conn = psycopg2.connect(
    host="database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com",
    port=5432,
    database="studentdb",
    user="postgres",
    password="Dev12345"
)

print("Connected successfully!")

conn.close()