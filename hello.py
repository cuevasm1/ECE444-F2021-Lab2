from flask import Flask, render_template
from datetime import datetime

# from flask_moment import Moment
# moment = Moment(app)

###
from flask_bootstrap import Bootstrap
app =Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    #return '<h1>Hello World!</h1>'
    #return render_template('index.html', current_time=datetime.utcnow())
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

if __name__=='__main__':
    app.run(debug=True)
