from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/api/users')
def get_users():
    users = [{'id': 1, 'username': 'sweety'},
             {'id': 2, 'username': 'pandey'}]
    response = Response(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run()