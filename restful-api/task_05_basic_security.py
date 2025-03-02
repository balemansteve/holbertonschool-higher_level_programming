#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "1234"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for Basic Authentication.
    Args:
        username (str): The provided username
        password (str): The provided password
    Returns:
        str or None: Returns the username if authentication is successful, otherwise None
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Handle GET request to a Basic Auth-protected endpoint.
    Returns:
        Response: A message indicating access has been granted.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=["POST"])
def login():
    """
    Handle user login and return a JWT token.
    Returns:
        Response: JSON object with the JWT token if credentials are valid,
                 otherwise an error message with status code 401.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)

    return jsonify({'error': "data invalid"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Handle GET request to a JWT-protected endpoint.
    Returns:
        Response: A message indicating access has been granted.
    """
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Handle GET request to an admin-only endpoint.
    Returns:
        Response: JSON object with access granted if the user is an admin,
                 otherwise an error message with status code 403.
    """
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token.
    Returns:
        Response: JSON object with an error message and status code 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token.
    Returns:
        Response: JSON object with an error message and status code 401.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token.
    Returns:
        Response: JSON object with an error message and status code 401.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked JWT token.
    Returns:
        Response: JSON object with an error message and status code 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle requests requiring a fresh JWT token.
    Returns:
        Response: JSON object with an error message and status code 401.
    """
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
