from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Ketan"
    l1 = list(name)
    d1 = {"name":"Satwik"}
    return render_template('index.html', name=name, l1=l1, d1=d1) 

@app.route('/info')
def info():
    return '<h1> Welcome to Info page</h1>'

@app.route('/friend/<name>')
def friend(name):
    return '<h1>This page is for my friend {}</h1>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)