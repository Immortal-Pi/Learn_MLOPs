import streamlit as st 
import pandas as pd

st.title('Streamlit Text Input')

name=st.text_input('Enter your name:')

age=st.slider('select your age:',0,100,25)

st.write(f'your age is :{age}')

options=['Python','Java','C++','JavaScript']
choice=st.selectbox('Choose your favourite language:',options)

if name:
    st.write(f'welcome {name}')


data={
    'Name':['Amruth','Akshath','Subhodh','Chiranth'],
    'Age':[20,21,22,23],
    'City':['New York','Los Angeles','Chicago','Houston'],
}
df=pd.DataFrame(data)
df.to_csv()
st.write(df)

uploaded_files=st.file_uploader('choose a csv file',type='csv')

if uploaded_files is not None:
    df=pd.read_csv(uploaded_files,encoding='utf-8')
    st.write(df)