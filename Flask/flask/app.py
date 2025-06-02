from flask import Flask
'''
It creates an instance of the flask app.
which will be our WSGI (Web Server Gateway Interface) application.
'''

## WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the best Flask Application! This is the home page."

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == '__main__':
    app.run(debug=True)