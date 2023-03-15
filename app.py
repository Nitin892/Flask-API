from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Set up a connection to MongoDB
client = MongoClient(
    'mongodb://localhost:27017/?readPreference=primary&directConnection=true&ssl=false')
# Create a new database
try:
    db = client['mydatabase']
except Exception as e:
    print(e)

# Create a new collection in the database
UserCollection = db["users"]


@app.route('/')
def index():
    return "Hello World!"

# Endpoint to retrieve all users


@app.route('/get', methods=['GET'])
def getUsers():
    # Get all users from the collection
    users = list(UserCollection.find())
    # Convert ObjectId to string for JSON serialization
    for user in users:
        user['_id'] = str(user['_id'])
    # Return the users as a JSON object
    return jsonify(users)

# Endpoint to create a new user


@app.route('/create_user', methods=['POST'])
def create_user():
    # Get the user data from the request JSON
    newuser = request.json

    # Create a new document for the user
    user = {
        "name": newuser['name'],
        "email": newuser['email'],
        "password": newuser['password']
    }

    # Insert the user document into the collection
    UserCollection.insert_one(user)

    # Return a success message and HTTP status code 201
    return {'message': 'successfully created'}, 201

# Endpoint to retrieve a single user by ID


@app.route('/users/<int:user_id>', methods=['GET'])
def getUser(user_id):
    # Find the user document by skipping to the correct index
    user = UserCollection.find_one(skip=user_id-1)

    # If the user document is found, convert the ObjectId to string and return as JSON
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)

    # Otherwise, return a 404 error with a JSON message
    return jsonify({'message': 'User not found'}), 404

# Endpoint to update a user by ID


@app.route('/update/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    # Find the user document by skipping to the correct index
    user = UserCollection.find_one(skip=user_id-1)

    # Get the updated user data from the request JSON
    data = request.json

    # Update the user document with the new data
    user["name"] = data["name"]
    user["email"] = data["email"]
    user["password"] = data["password"]

    # Update the collection with the new user document
    UserCollection.update_one({"_id": user["_id"]}, {'$set': user})

    # Return a success message as JSON
    return {"message": "success"}

# Endpoint to delete a user by ID


@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    # Find the user document by skipping to the correct index
    user = UserCollection.find_one(skip=user_id-1)

    # Delete the user document from the collection
    UserCollection.delete_one({"_id": user["_id"]})

    # Return a success message as JSON
    return {"message": 'success'}


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
