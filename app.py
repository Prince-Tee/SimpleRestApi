from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25}
]

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((item for item in data if item["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user['id'] = len(data) + 1
    data.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
