from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')

    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return f"Requête exécutée : {query}"

if __name__ == '__main__':
    app.run(debug=True)