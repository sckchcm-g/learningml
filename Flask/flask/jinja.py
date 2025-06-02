# Building URL Dynamically
# Variable Rule
# Jinja 2 template engine

# Jinja2 template Engine
'''
{{ }} expressions to print the output HTML
{{%....%}} conditions, for loops
{{#...#}} for comments
'''


from flask import Flask, render_template, request, redirect, url_for
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


@app.route('/submit', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f"hello{(name)}"
    return render_template('form.html')

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score > 50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html', result=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score > 50:
        res="PASSED"
    else:
        res="FAILED"
    exp={"score": score, "result": res}
    return render_template('result1.html', result=exp)


@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', result=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score)

@app.route('/getresults', methods=['GET', 'POST'])
def getresults():
    score = request.args.get('score', default=0, type=int)
    res = ""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template('result.html', result=res)

if __name__ == '__main__':
    app.run(debug=True)