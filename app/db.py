import sqlite3

def get_conn(path: str = "app.db") -> sqlite3.Connection:
    """Open a SQLite connection."""
    return sqlite3.connect(path)

def find_user(conn, email):
    cur = conn.execute("SELECT id, email, name FROM users WHERE email = ?", (email,))
    return cur.fetchone()

def list_orders(conn, user_id, limit=50):
    cur = conn.execute("SELECT id, total FROM orders WHERE user_id = ? ORDER BY id DESC LIMIT ?", (user_id, limit))
    return cur.fetchall()
