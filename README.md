

This is a simple Flask application that allows you to manage a collection of users in a MongoDB database. The application provides endpoints to create, retrieve, update, and delete users.

SETUP

1. Install Python 3
2. Install Flask and PyMongo libraries
     * Open your terminal and run the following command: pip install flask pymongo
3. Install MongoDB
   * Follow the installation instructions for your operating system at https://docs.mongodb.com/manual/installation/
4. Start the MongoDB server
   * Open a new terminal window and run the following command: mongod
5. Clone the repository or download the source code
6. Open a terminal and navigate to the root directory of the application
7. Run the following command to start the application: python app.py
8. Open a web browser and navigate to http://localhost:5000 to access the application

USAGE
* Endpoint to retrieve all users
     * GET http://localhost:5000/get
     * Returns a JSON object containing all users in the collection
       
* Endpoint to create a new user
     * POST http://localhost:5000/create_user
     * Request body should be a JSON object containing the user data (name, email, and password)
     * Returns a success message with HTTP status code 201
     
* Endpoint to retrieve a single user by ID
     * GET http://localhost:5000/users/int:user_id
     * Replace int:user_id with the ID of the user you want to retrieve
     * Returns a JSON object containing the user data
     
* Endpoint to update a user by ID
     * PUT http://localhost:5000/update/int:user_id
     * Replace int:user_id with the ID of the user you want to update
     * Request body should be a JSON object containing the updated user data (name, email, and password)
     * Returns a success message as JSON
    
* Endpoint to delete a user by ID
     * DELETE http://localhost:5000/delete/int:user_id
     * Replace int:user_id with the ID of the user you want to delete
     * Returns a success message as JSON








