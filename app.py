from flask import Flask
app = Flask(__name__)   #Setting the app to an instance class of Flask

#Creating routes using decorators
@app.route("/")
@app.route("/home") #Using main route for home page
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about") #Using "/" route for home page
def about():
    return "<h1>About Page!</h1>"


#Running app directly using python filename.py
if __name__ == '__main__':
    app.run(debug=True)