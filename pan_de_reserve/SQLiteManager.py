import sqlite3
from typing import List, Tuple, Any


class SQLiteManager:
    def __init__(self, db_path: str):
        """
        初期化時にデータベース接続を設定します。
        :param db_path: SQLiteデータベースのファイルパス
        """
        self.db_path = db_path

    def query(self, sql: str, params: Tuple = ()) -> List[Tuple[Any, ...]]:
        """
        SQLクエリを実行してデータを取得します。
        :param sql: 実行するSQLクエリ
        :param params: クエリのパラメータ（タプル形式）
        :return: クエリ結果のリスト
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
            return []

    def execute(self, sql: str, params: Tuple = ()) -> int:
        """
        SQLコマンドを実行（INSERT, UPDATE, DELETEなど）します。
        :param sql: 実行するSQLコマンド
        :param params: コマンドのパラメータ（タプル形式）
        :return: 影響を受けた行数
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
            return -1


"""
usage
db_manager = SQLiteManager("example.db")

# テーブル内のデータを取得
sql_query = "SELECT * FROM Reservations WHERE is_recieved = ?"
params = (1,)  # 条件付きパラメータ
results = db_manager.query(sql_query, params)

for row in results:
    print(row)

# 新しい予約を挿入
insert_sql = 
INSERT INTO Reservations (id, recieve_time, customer_name, customer_phone_number, is_recieved)
VALUES (?, ?, ?, ?, ?)

params = (1, "2024-12-01 10:00:00", "John Doe", "123-456-7890", 0)
rows_affected = db_manager.execute(insert_sql, params)
print(f"Rows affected: {rows_affected}")

# 既存の予約を更新
update_sql = "UPDATE Reservations SET is_recieved = ? WHERE id = ?"
params = (1, 1)
rows_affected = db_manager.execute(update_sql, params)
print(f"Rows affected: {rows_affected}")
"""