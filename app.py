from web_app import create_app

#Running app directly using python filename.py
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)