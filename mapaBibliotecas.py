import streamlit as st
import pandas as pd
import numpy as np

folder = "F:/Google Drive/Proyectos/UCongreso - Profesorado para profesionales/Primer semestre/Instituciones Educativas/Para presentaciones grupales/Participación/"

df = pd.read_csv(folder + 'biblioteca_popular.csv')

st.header('Sitios culturales - Bibliotecas populares')

df = df.query("Departamento == 'San Rafael'")
df = df[['lat','lon']]
#print(df.head())
st.map(df)
