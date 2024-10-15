from flask import Flask, jsonify, request
from helper import execute_query

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def flaskea():
    return 'Welcome to the Flaskea database!'

# 1. get all users
# Define routes
@app.route('/user', methods=['GET'])
def get_users():
    users = execute_query("SELECT * FROM Users")
    if users:
        return jsonify(users)
    
    elif not users:
        return jsonify({'message': 'No users found'})

# 2. get user by id
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = execute_query(f"SELECT * FROM Users WHERE UserID = {id}")
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'No matching user found'})

# 3. get all products
@app.route('/product', methods=['GET'])
def get_products():
    products = execute_query("SELECT * FROM Products")
    if products:
        return jsonify(products)  
    elif not products:
        return jsonify({'message': 'No products found'})

# # 4. get product by id
@app.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = execute_query(f"SELECT * FROM Products WHERE ProductID = {id}")
    if product:
        return jsonify(product)
    elif not product:
        return jsonify({'message': 'No matching product found'})
    

#5 get cart item by user id
@app.route('/cart/<int:id>', methods=['GET'])
def get_cart(id):
    cart = execute_query(f"SELECT * FROM CartItems WHERE UserID = {id}")
    if cart:
        return jsonify(cart)
    elif not cart:
        return jsonify({'message': 'No matching cart found'})
    
#6 create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('Name')
    email = data.get('Email')
    password = data.get('Password')
    query = f"INSERT INTO Users (Name, Email, Password) VALUES ('{name}', '{email}', '{password}')"
    execute_query(query)
    return jsonify({'message': 'User created successfully'})

#7 update a specific user email
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    email = data.get('Email')
    query = f"UPDATE Users SET Email = '{email}' WHERE UserID = {id}"
    execute_query(query)
    return jsonify({'message': 'User updated successfully'})

#8 create an API of your choice
#Thank you for making the necessary changes for the developer and 
# verify that the changes has been done successfully. 
@app.route('/api', methods=['GET'])
def get_api():
    return jsonify('Thank you for making the necessary changes, Your changes has been saved successfully.')

if __name__ == '__main__':
    app.run(debug = False)