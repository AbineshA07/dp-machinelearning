import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is App build a Machine Learning Model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
st.write('**x**')
x = df.drop('species', axis = 1)
x

st.write('**y**')
y = df.species
y
with st.expender('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g',color = 'species')
