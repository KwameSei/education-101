from flask import Flask, render_template
app = Flask(__name__)   #Setting the app to an instance class of Flask

#Creating routes using decorators
@app.route('/')
@app.route('/home') #Using main route for home page
def home():
    return render_template('home.html')

@app.route('/about') #Using "/" route for home page
def about():
    return render_template('about.html')


#Running app directly using python filename.py
if __name__ == '__main__':
    app.run(debug=True)