# Importing the required libraries
from flask import Flask,jsonify

# Importing the required functions from the second assignment file
from data.second_assignment import read_data,mod,hello

# Defining the flask app
app=Flask(__name__)

# Defining the routes
@app.route('/api/printHello',methods=['GET']) # Defining the route for the hello world 
def printHello():
    data=hello()
    return jsonify(data)

@app.route('/api/originalRecepie',methods=['GET']) # Defining the route for the original recepie
def printData():
    data=read_data()
    return jsonify(data)

@app.route('/api/modifiedRecepie',methods=['GET']) # Defining the route for the modified recepie
def printModData():
    data=mod()
    return jsonify(data)

# Defining the main function
if __name__=='__main__':
    app.run(debug=True,port=80)