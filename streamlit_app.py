import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This is App build a Machine Learning Model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
df
