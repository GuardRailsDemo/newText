import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_user_info(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable: unsanitized input directly in query string
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/user')
def user():
    username = request.args.get('username', '')
    data = get_user_info(username)
    return {"user_info": data}

if __name__ == '__main__':
    app.run(debug=True)
