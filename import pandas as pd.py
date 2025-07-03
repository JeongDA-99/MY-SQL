import pandas as pd
import sqlite3
# 변환할 csv 파일 경로
csv_file = '/Users/ms_j/Downloads/videos.csv'
db_file = 'videos.db'
table_name = 'videos'
df = pd.read_csv(csv_file)
conn = sqlite3.connect(db_file)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
