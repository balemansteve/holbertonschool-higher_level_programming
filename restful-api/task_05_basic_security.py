"""
This script creates a Flask API with authentication mechanisms using Basic Auth and JWT.
It provides endpoints for protected access, user authentication, and role-based authorization.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret_key_HolbertonC24!'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {}

@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for Basic Authentication.
    Args:
        username (str): The provided username
        password (str): The provided password
    Return:
        str or None: Returns the username if authentication is successful, otherwise None
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@auth.error_handler
def unauthorized():
    """
    Handle unauthorized access for Basic Authentication
    Args:
        None
    Return:
        Response: JSON object with an error message and status code
    """
    return jsonify({"error": "Unauthorized access"}), 401

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Handle GET request to a Basic Auth-protected endpoint
    Args:
        None
    Return:
        Response: JSON object with a message
    """
    return jsonify(message="Basic Auth: Access Granted")

@app.route('/login', methods=['POST'])
def login():
    """
    Handle user login and return a JWT token.
    Args:
        None (data is extracted from the request body)
    Return:
        Response: JSON object with the JWT token if credentials are valid,
                 otherwise an error message with status code
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Handle GET request to a JWT-protected endpoint
    Args:
        None
    Return:
        Response: JSON object with an access message
    """
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Handle GET request to an admin-only endpoint
    Args:
        None
    Return:
        Response: JSON object with access granted if the user is an admin,
                 otherwise an error message with status code
    """
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted")

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token
    Args:
        err (str): The error message
    Return:
        Response: JSON object with an error message and status code
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token
    Args:
        err (str): The error message
    Return:
        Response: JSON object with an error message and status code
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token
    Args:
        err (str): The error message
    Return:
        Response: JSON object with an error message and status code
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked JWT token
    Args:
        err (str): The error message
    Return:
        Response: JSON object with an error message and status code
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle requests requiring a fresh JWT token
    Args:
        err (str): The error message
    Return:
        Response: JSON object with an error message and status
    """
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
