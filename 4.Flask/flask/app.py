from flask import Flask


'''
it creates an instance of the Flask class,
which will be your WSGI (Web server Gateway Interface) application.
'''
## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask page. This should be amazing "

@app.route("/index")
def welcome_index():
    return "Welcome to the index page"

if __name__=='__main__':
    app.run(debug=True)