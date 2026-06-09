import sqlite3

class Database:
    def __init__(self, db_path="cars.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS seen (
            url TEXT PRIMARY KEY
        )
        """)
        self.conn.commit()

    def is_seen(self, url: str) -> bool:
        self.cursor.execute("SELECT 1 FROM seen WHERE url=?", (url,))
        return self.cursor.fetchone() is not None

    def add(self, url: str):
        self.cursor.execute("INSERT OR IGNORE INTO seen (url) VALUES (?)", (url,))
        self.conn.commit()
