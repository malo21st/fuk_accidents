import streamlit as st
import streamlit.components.v1 as components

with open("acc_map.html", mode="r") as f:
    html_string = f.read() 

#wrap all your code in this method and you should be done
def app():
    components.html(html_string, width=st.javascript('window.screen.width') ,height=600)
#     components.html(html_string, width=700, height=500)
