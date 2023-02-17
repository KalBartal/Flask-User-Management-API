# Flask User Management API

[ ![Flask User Management API](./image.png)](https://kalbartal.net/building-a-restful-api-with-flask-and-sqlalchemy/)

I have a step by step walkthrough for this code on my [my blog](https://kalbartal.net/building-a-restful-api-with-flask-and-sqlalchemy/).

This repository contains code for a Flask API that can be used to manage user information. The API implements the following routes:

* GET /users - to get list of all users in the database
* GET /users/<int:user_id> - to get a specific user by id
* POST /users - to create a new user
* PUT /users/<int:user_id> - to update a specific user
* DELETE /users/<int:user_id> - to delete a specific user

## Requirements

This API requires the following libraries:

* Flask 0.12.2 or higher
* SQLAlchemy 1.1.11 or higher
* Werkzeug 0.12.2 or higher

## Installation

Clone the repository:

```
git clone https://github.com/username/flask-user-management.git
```

Navigate to the repository directory:

```
cd flask-user-management
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

## Usage

API endpoints can be tested with curl or any other HTTP client. Examples below use curl.

**GET /users**

Get all users in the database.

```
curl -X GET http://localhost:5000/users
```

**GET /users/<int:user_id>**

Get a user with the specified ID.

```
curl -X GET http://localhost:5000/users/<user_id>
```

**POST /users**

Add a new user to the database.

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "password": "password"}' http://localhost:5000/users
```

**PUT /users/<int:user_id>**

Update a user with the specified ID.

```
curl -X PUT -H "Content-Type: application/json" -d '{"name": "John Smith", "email": "john@example.com", "password": "strongpassword"}' http://localhost:5000/users/<user_id>
```

**DELETE /users/<int:user_id>**

Delete a user with the specified ID.

```
curl -X DELETE http://localhost:5000/users/<user_id>
```

## License

This project is released under the [MIT License](https://choosealicense.com/licenses/mit/).
