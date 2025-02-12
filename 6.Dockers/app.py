import flask
import pickle

from flask import Flask,request
import os 
import pandas as pd 
import numpy as np 
import pickle 

app=Flask(__name__)

# load the classifier model
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


@app.route('/',methods=['GET'])
def home():
    return 'Hello World'

@app.route('/predict')
def redict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return f'the predicted value is {prediction}'

@app.route('/predict_file',methods=['POST'])
def redirect_note_authentication_file():
    df=pd.read_csv(request.files.get(''))
    prediction=classifier.predict(df.iloc[:,:-1])
    return f'The predicted values is {list(prediction)}'




if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)