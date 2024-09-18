from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Connexion à la base de données PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            database="northwind",
            user="postgres",
            password="postgres",
            port=5432
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def index():
    conn = connect_db()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM products')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()

    return f'There are {count} products in the database.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
