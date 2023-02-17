# Import Libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Create Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)


# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'


# Create the tables of the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return 'Hello World!'


# Route to get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    # Query the database to get all users
    users = User.query.all()

    # Return a JSON response with the data of all users
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])


# Route to get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    # Retrieve user object with the given id
    user = User.query.get(user_id)
    # Check if user exists, return 404 error if not
    if not user:
        return jsonify({'message': 'User not found'}), 404
    # Return user information in JSON format
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})


# Route to handle POST requests for creating users
@app.route('/users', methods=['POST'])
def create_user():
    # Get JSON data from request
    data = request.get_json()
    # Check if the user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists!'}), 400
    # Create new User object with data
    new_user = User(name=data['name'], email=data['email'],
                    password=generate_password_hash(data['password'], method='sha256'))
    # Add new user to database session
    db.session.add(new_user)
    # Commit changes to database
    db.session.commit()
    # Return success message
    return jsonify({'message': 'User created successfully!'})


# Route to handle PUT requests for updating user info
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Get the user with the specified ID from the database
    user = User.query.get(user_id)
    # If the user is not found, return a 404 error response
    if not user:
        return jsonify({'message': 'User not found'}), 404
    # Parse request data as JSON
    data = request.get_json()
    # Update user's name, email, and password with new values
    user.name = data['name']
    user.email = data['email']
    user.password = data['password']
    # Commit changes to database
    db.session.commit()
    # Return success message
    return jsonify({'message': 'User updated successfully!'})


# Route to handle DELETE requests for deleting user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Get the user with the specified ID from the database
    user = User.query.get(user_id)
    # If the user is not found, return a 404 error response
    if not user:
        return jsonify({'message': 'User not found'}), 404
    # Detach user from the current session
    db.session.expunge(user)
    # Delete user from database
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to delete user: {}'.format(str(e))}), 500
    # Return success message
    return jsonify({'message': 'User deleted successfully!'})


# Run application if file is run as main
if __name__ == '__main__':
    app.run(debug=False)
