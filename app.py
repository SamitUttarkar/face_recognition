from flask import Flask, redirect,url_for

## WSGI application is created it is a standard for communitacting with the web server
app = Flask(__name__)

# the decorator hels us the run the function below it and it defines/creates the url
@app.route('/')
def welcome():
    return "Welcome to my face recognition"

@app.route('/success/<int:score>')
def success(score):
    return "The score of our model is" + str(score)

@app.route('/error/<int:score>')
def error(score):
    return "The error of our model is" + str(score)

# what if we want to show a different score for less score and for more score
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks <50:
        result = 'error'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug = True)