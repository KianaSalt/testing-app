from flask import Flask           # import flask framework
app = Flask(__name__)

@app.route("/")                   # Route for the homepage
def homeo():                      
    return "This is the homepage"

@app.route("/booking")                   # Route for the booking page
def booking():                      
    return "This is the booking page"
    
@app.route("/end")                   # Route for the homepage
def last():                      
    return "This is the end/last page"