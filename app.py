from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/test-db")
def test_db():
    import os
    import sqlite3

    path = "/data/digital_collections_ocfl/ark_data.db"
    if not os.path.exists(path):
        return f"File not found: {path}", 500
    try:
        con = sqlite3.connect(path)
        con.execute("SELECT 1")
        con.close()
        return "DB accessible", 200
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run()
