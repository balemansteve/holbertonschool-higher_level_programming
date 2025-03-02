"""
This script creates a simple Flask API with multiple endpoints to manage user data.
It supports retrieving, adding, and listing users in memory.
"""


from flask import Flask, jsonify, request

app = Flask(__name__)
    
users = {}

@app.route('/')
def home():
    """
    Handle GET request to the root endpoint.
    Args:
        None
    Return:
        str: Message
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """
    Handle GET request to retrieve a list of all registered usernames.
    Args:
        None
    Return:
        Response: JSON list of usernames
    """
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """
    Handle GET request to check API status.
    Args:
        None
    Return:
        str: Message
    """
    return "OK"

@app.route('/users/<username>')
def getuser(username):
    """
    Handle GET request to retrieve user details by username
    Args:
        username (str): The username to look up
    Return:
        Response: JSON object containing user data if found,
        otherwise an error message with status 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({
            "error": "User not found"
            }), 404

@app.route('/add_user', methods = ['POST'])
def add_user():
    """
    Handle POST request to add a new user.
    Args:
        None (data is extracted from the request body)
    Return:
        Response: JSON object with a success message and the user data if successful, 
                 otherwise an error message with status 400 if the username is missing.
    """
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({
            "error": "Username is required"
            }), 400
    users[username] = {
        "username": username.lower(),
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
        }), 201

if __name__ == '__main__':
    app.run(debug=False)
