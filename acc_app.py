import streamlit as st
import acc_heatmap, acc_map #, acc_table
from multipage import MultiPage
import itertools

count = itertools.count()

def set_mode(mode):
    if next(count) == 0:
        st.set_page_config(layout=mode)
        print(f"*** set layout {mode} ***")

def main():
    # Create an instance of the app 
    app = MultiPage()

    # Add all your applications (pages) here
    app.add_page("発生時間帯", acc_heatmap.app)
    app.add_page("事故マップ", acc_map.app)
    # app.add_page("事故データ", acc_table.app)

    # The main app
    app.run()

if __name__ == "__main__":
    set_mode("wide")
    main()
