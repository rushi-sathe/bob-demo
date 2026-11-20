from flask import Flask, request, jsonify
from database import get_connection, create_table
from config import SECRET_KEY

app = Flask(__name__)

# WARNING: INTENTIONALLY INSECURE DEMO
app.secret_key = SECRET_KEY

create_table()


@app.route("/")
def home():
    return "CodeGuard AI Vulnerable Demo Application"


@app.route("/search")
def search_users():

    username = request.args.get("username", "")

    conn = get_connection()

    # WARNING: INTENTIONALLY VULNERABLE
    # User input is directly inserted into SQL.
    query = (
        "SELECT * FROM users WHERE username = '%s'"
        % username
    )

    results = conn.execute(query).fetchall()

    conn.close()

    return jsonify([
        {
            "id": user[0],
            "username": user[1],
            "email": user[2]
        }
        for user in results
    ])


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
