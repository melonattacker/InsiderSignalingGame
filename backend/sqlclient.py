import mysql.connector as mydb

def connect():
    # コネクションの作成
    conn = mydb.connect(
        host='mysql',
        port='3306',
        user='mysql',
        password='WmE3PQVuBEW3Br6d',
        database='employee',
        charset='utf8'
    )
    return conn

def query_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee;")
    rows = cur.fetchall() # 全ての従業員データを取得
    return rows

# rows = query_employees()
# print(type(rows))
# print(rows)