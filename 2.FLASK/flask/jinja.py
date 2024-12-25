from flask import Flask, render_template,request,redirect,url_for


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


# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name'] 
#         return f'Hello {name} !'
#     return render_template('form.html')

### Jinja2 template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions. for loops
{#...#} this is for comments
'''
@app.route('/success/<int:score>')
def sucess(score):
    #return f'The marks you got is '+str(score) 
    res=""
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'

    exp={'score':score,'res':res}
    return render_template('result.html',results=exp)

@app.route('/successres/<int:score>')
def successres(score):
    #return f'The marks you got is '+str(score) 
    res=""
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'

    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)

##if condition 
@app.route('/successif/<int:score>')
def sucessid(score):
    return render_template('results.html',results=score)

##if condition 
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['science'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+math+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))
if __name__=='__main__':
    app.run(debug=True)