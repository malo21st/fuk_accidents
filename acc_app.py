import streamlit as st
import acc_heatmap, acc_map, acc_table

# Create an instance of the app 
app = MultiPage()

# Add all your applications (pages) here
app.add_page("発生時間帯", acc_heatmap.app)
app.add_page("事故マップ", acc_map.app)
# app.add_page("事故データ", acc_table.app)

# The main app
app.run()
