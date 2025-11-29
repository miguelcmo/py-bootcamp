# import packages and modules
from flask import Flask # Flask es una clase - class
from flask import render_template

# create a new app instance from Flask
app = Flask(__name__) # keywords - reserved variables

# defining a default route
@app.route('/')
def index():
    return f'This is my firts app!'

# defining a route that will be use a template to render the page
@app.route('/hello/')
@app.route('/hello/<name>') # /<variable> define a route variable
def hello(name=None):
    return render_template('hello.html', person=name)

# leave this section at the end
if __name__ == "__main__": # is True when we execute the file directly from python $ python app.py
    app.run(debug=True) # flask --app app run