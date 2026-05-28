import psycopg2

conn = psycopg2.connect(
    host="database-1.cpo2wows09qf.ap-south-1.rds.amazonaws.com",
    database="postgres",
    user="postgres",
    password="Dev12345",
    port=5432
)

cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())

conn.close()