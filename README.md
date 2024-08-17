
# Flask REST API

This project is a simple REST API built using Flask, a lightweight web framework for Python. It demonstrates how to create basic CRUD (Create, Read, Update, Delete) operations for managing user data. The API includes endpoints to get a list of users, get a specific user by ID, and add a new user.

## Features

- **Get all users**: Retrieve a list of all users.
- **Get a user by ID**: Retrieve details of a specific user by their unique ID.
- **Add a new user**: Add a new user with a unique ID and user data.

## Prerequisites

- **Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Flask**: Install Flask using pip (Python's package manager).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/flask-rest-api.git
   cd flask-rest-api
   ```

2. **Install Dependencies**

   Create a virtual environment to manage dependencies and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Install Flask:

   ```bash
   pip install Flask
   ```

## Running the Application

1. **Start the Flask Application**

   Run the Flask application with:

   ```bash
   python app.py
   ```

   The server will start and be accessible at `http://127.0.0.1:5000/`.

2. **Access the API Endpoints**

   - **Get All Users**: `GET http://127.0.0.1:5000/users`
   - **Get User by ID**: `GET http://127.0.0.1:5000/users/<user_id>`
   - **Add a New User**: `POST http://127.0.0.1:5000/users` with JSON body
   
   Example JSON body for adding a user:

   ```json
   {
     "name": "Alice Smith",
     "age": 28
   }
   ```

## API Endpoints

### Get All Users

- **URL**: `/users`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    [
      {"id": 1, "name": "John Doe", "age": 30},
      {"id": 2, "name": "Jane Doe", "age": 25}
    ]
    ```

### Get User by ID

- **URL**: `/users/<user_id>`
- **Method**: `GET`
- **URL Params**: 
  - **Required**: `user_id=[integer]`
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {"id": 1, "name": "John Doe", "age": 30}
    ```
- **Error Response**:
  - **Code**: 404
  - **Content**:
    ```json
    {"message": "User not found"}
    ```

### Add a New User

- **URL**: `/users`
- **Method**: `POST`
- **Data Params**: 
  - **Required**: `name=[string]`, `age=[integer]`
- **Success Response**:
  - **Code**: 201
  - **Content**:
    ```json
    {
      "id": 3,
      "name": "Alice Smith",
      "age": 28
    }
    ```

## Project Structure

- **app.py**: The main Python file where the Flask app is defined and routes are created.
- **venv/**: Virtual environment directory (created during setup).

## Troubleshooting

- **Flask Not Found**: Ensure Flask is installed in your virtual environment.
- **Port Conflict**: The default port is 5000. If another application uses this port, change it in the `app.run()` method in `app.py`.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.