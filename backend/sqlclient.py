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

def insert_employee(name, action):
    conn = connect()
    cur = conn.cursor()
    print(name, action)
    cur.execute("INSERT INTO employee (name, action) VALUES (%s, %s)", (name, action))
    conn.commit()
    cur.close()
    conn.close()
    return "ok"

def query_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee;")
    rows = cur.fetchall() # 全ての従業員データを取得
    cur.close()
    conn.close()
    return rows