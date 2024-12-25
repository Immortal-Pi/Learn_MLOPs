from flask import Flask, render_template,request


'''
it creates an instance of the Flask class,
which will be your WSGI (Web server Gateway Interface) application.
'''
## WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>welcome to this flask page. This should be amazing</H1></html>"

@app.route("/index",methods=['GET'])
def welcome_index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name'] 
        return f'Hello {name} !'
    return render_template('form.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        name=request.form['name'] 
        return f'Hello {name} !'
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)