import flask
import pickle

from flask import Flask
import os 
app=Flask(__name__)

# load the classifier model
# pickle_in=open('classifier.pkl','rb')
# classifier=pickle.load(pickle_in)


@app.route('/',methods=['GET'])
def home():
    return 'Hello World'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)