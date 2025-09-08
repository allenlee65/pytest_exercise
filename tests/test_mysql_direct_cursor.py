import pymysql
# DictCursor 需要從 pymysql.cursors import
from pymysql.cursors import DictCursor

db_settings = {
    "user": "root",
    "password": "123Qwe!!",
    "host": "127.0.0.1",
    "database": "test_db",
    "read_timeout" : 5,
    # 預設是 Cursor，改為 DictCursor
    "cursorclass": DictCursor
}


with pymysql.connect(**db_settings) as connection:
    with connection.cursor() as cursor:
        select_sql = "SELECT userId, email, pw FROM User;"	    
        cursor.execute(select_sql)
	
        result = cursor.fetchall()
        for row in result:
            # 這裡便可以用 key 來取值了
	        print(row["userId"], row["email"], row["pw"]) # type: ignore