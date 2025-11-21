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

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g',color = 'species')

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscode', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('Male', 'Female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 32.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)

  # Create a DataFrame for the input features
  data = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}

  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, X], axis=0)



