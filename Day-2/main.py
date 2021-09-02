from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    l1 = ["Vishwajeet","Ravi","Sunil","Micky"]
    return render_template('base.html', l1=l1)

@app.route('/friend/<name>')
def friend(name):
    return render_template('friend.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)