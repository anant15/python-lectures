#print("Hello World!")

# flask basics
from flask import Flask, jsonify, request
app = Flask(__name__, static_url_path="/static")
# If this file is getting directly run from the terminal,
# by default  __name__ will be set to "__main__" . Otherwise, 
# if we are importing this file in some other Python script, 
# then it will different. We will get to see it's importance later.

# Function decorator
# @app.route("/") # "/" is one of the end-points
# def hello():
#     # function name can be anything
#     return "Hello"

# # Example of creating our own API
users = [{'id':2, 'name':'Anne', 'age':20}, {'id':1, 'name':'Cathy', 'age':21}]

@app.route("/users/")
def get_users():
    return jsonify(users) # jsonify is used to convert the dict to string
    # you can only send a string

# # Creating a dynamic route, search user by ID
@app.route("/users/id/<id>")
def get_user(id):
    result = [u for u in users if u['id'] == int(id)] # check the datatype
    result = list(filter(lambda u: u['id'] == int(id), users)) # check the data type here, remember input()
    print(result) # the output of this will be seen in the terminal
    return jsonify(result)

# HTML end-points
@app.route("/")
def index():
    return app.send_static_file("index.html")
    # if we change the content of the html file, we don't need to re-start the server - app.py

# # Another end-point, search by some other variable
@app.route('/users/name/<name>')
def getUser(name):
    result = [u for u in users if u['name']==name]
    #result = list(filter(lambda u: u['id']==id, users)) # check the data type here, remember input()
    return jsonify(result)

# #Adding some Javascipt to the code

if __name__ == "__main__":
    app.run() # runs the server


