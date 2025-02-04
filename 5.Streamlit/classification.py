# basic ml project on streamlit 
import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df, iris.target_names


data,target=load_data()
print(target)

model=RandomForestClassifier()
model.fit(data.iloc[:,:-1],data['species'])

st.sidebar.title('Input Features')
sepal_length=st.sidebar.slider('Sepal Length',float(data['sepal length (cm)'].min()),float(data['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider('Sepal width',float(data['sepal width (cm)'].min()),float(data['sepal width (cm)'].max()))
petal_length=st.sidebar.slider('Sepal length',float(data['petal length (cm)'].min()),float(data['petal length (cm)'].max()))
petal_width=st.sidebar.slider('Sepal width',float(data['petal width (cm)'].min()),float(data['petal width (cm)'].max()))


input_data=[[sepal_length,sepal_width,petal_length,petal_width]]

## Prediction
prediction=model.predict(input_data)
predicted_Species=target[prediction[0]]

st.write('Prediction')
st.write(f'The predicted species: {predicted_Species}')