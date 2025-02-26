from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample fruit data
fruits = [
    {"id": 1, "name": "Apple", "color": "Red"},
    {"id": 2, "name": "Banana", "color": "Yellow"},
    {"id": 3, "name": "Orange", "color": "Orange"}
]

# Home route
@app.route('/')
def home():
 return jsonify(fruits), 200

# Get all fruit
@app.route('/fruits', methods=['GET'])
def get_fruits():
    return jsonify(fruits), 200

# Get fruit by ID
# App Route with Method, Method is GET, and we are passing fruit_id as parameter.
@app.route('/fruits/<int:fruit_id>', methods=['GET'])
# Define function get_fruit with fruit_id as parameter.
def get_fruit(fruit_id):
# next is function that iterates (expression for variable in iterable if condition) else it returns None by default.
    fruit = next((f for f in fruits if f["id"] == fruit_id), None)
# return statement with jsonify in case of API.
    return jsonify(fruit) if fruit else jsonify({"error": "Fruit not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
