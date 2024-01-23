from flask import Flask

## WSGI application is created it is a standard for communitacting with the web server
app = Flask(__name__)

# the decorator hels us the run the function below it and it defines the url
@app.route('/')
def welcome():
    return "Welcome to my face recognition"

@app.route('/members')
def members():
    return "Welcome to my face recognition members"

if __name__ == '__main__':
    app.run(debug = True)