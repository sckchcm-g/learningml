from flask import Flask, render_template, request
'''
It creates an instance of the flask app.
which will be our WSGI (Web Server Gateway Interface) application.
'''

## WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "<HTML><h1>Welcome to the best Flask Application! This is the home page.</h1></HTML>"

@app.route('/about', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello{(name)}"
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)