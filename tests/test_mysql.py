import pymysql

db_settings = {
    ### DB Connection information
    "user": "root",
    "password": "123Qwe!!",
    "host": "127.0.0.1",

    ### 選填的部分
    # 一個 SQL Server 可以存在多個 Schema，一般來說會設定預設應用的 Schema
    # 若需要使用 SQL Server 內其他 Database，在 SQL 指定即可
    "database": "test_db",

    # 預設為 3306，若沒有改用其他 port，這個可以不填
    "port": 3306,

    # 設定讀取時數據庫未能返回響應的最大時間，會觸發超時錯誤。
    # 對於避免應用程式長時間阻塞或等待，我認為是很重要的設定。特別是測試需要大量讀取 DB 的情況。
    # 選擇適當的 read timeout 需要根據應用情況和需求進行評估。
    # 通常來說，可以從 5 秒到 30 秒之間進行調整，然後根據測試和實際使用情況進行微調。
    "read_timeout": 5,
}

# 連接 MySQL Server，執行程式碼後會自動關閉
with pymysql.connect(**db_settings) as connection:

    # 遊標（Cursor）是一個用於執行 SQL 查詢和操作數據的機制
    # 啟用 Cursor，在程式碼執行完畢後會自行關閉
    with connection.cursor() as cursor:
        select_sql = "SELECT userId, email, pw FROM User;"

        # 若沒有設定預設 database 時，需要在 SQL 指定用哪個 database 的 table
        # select_sql = "SELECT userId, email, pw FROM <schema>.user;"

        # 執行 SQL
        cursor.execute(select_sql)

        # 應用 Cursor 讀取所有資料
        result = cursor.fetchall()
        for row in result:
            print(row[0], row[1], row[2])