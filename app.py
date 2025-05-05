import streamlit as st
import pandas as pd

st.set_page_config(page_title="Brassaco Adm", page_icon="icon.png", layout="wide")
st.logo('logo.png', icon_image='icon.png', size='large')

def Dashboard():
    st.title("Dashboard")
    st.write("Welcome to the Brassaco Adm Dashboard")



pg = st.navigation([ Dashboard,  'Despesas.py', 'Receitas.py', 'Compras.py'])
pg.run()


