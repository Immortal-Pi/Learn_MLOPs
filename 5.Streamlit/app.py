import streamlit as st 
import pandas as pd 
import numpy as np 


## title of the application 
st.title('Hello Streamlit')


## display a simple text 
st.write('this is a simple text')

## create a simple dataframe 
df=pd.DataFrame({
    'first':[1,2,3,4,5],
    'second':[7,8,9,0,1]
})

## displat the dataframe 
st.write('Here is the dataframe')
st.write(df)

## create a line chart 

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)