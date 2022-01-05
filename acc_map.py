import streamlit as st
import streamlit.components.v1 as components

@st.cache
def load_map_html(html_file):
    with open(html_file, mode="r") as f:
        return f.read()
    
html_string = load_map_html("acc_map.html")

#wrap all your code in this method and you should be done
def app():
    components.html(html_string, width=800 ,height=600)
#     components.html(html_string, width=700, height=500)
