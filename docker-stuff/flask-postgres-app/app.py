from flask import Flask, request, render_template
import psycopg2
import os
import time
app = Flask(__name__)

# Database connection settings from environment variables
DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DB_NAME = os.environ.get("POSTGRES_DB", "notesdb")
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "password")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

def wait_for_db(max_retries=10, delay=3):
    for i in range(max_retries):
        try:
            conn = get_connection()
            conn.close()
            print("✅ Database is ready!")
            return
        except Exception as e:
            print(f"⏳ Waiting for database... ({i+1}/{max_retries})")
            time.sleep(delay)
    raise Exception("Database not ready after retries")

# Ensure the table exists
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_connection()
    cur = conn.cursor()

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            cur.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
            conn.commit()

    cur.execute("SELECT content FROM notes")
    notes = cur.fetchall()

    cur.close()
    conn.close()
    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    wait_for_db()
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)

