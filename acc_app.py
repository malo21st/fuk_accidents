import streamlit as st
import acc_heatmap, acc_map #, acc_table
from multipage import MultiPage
import itertools
# from PIL import Image

count = itertools.count()

def set_mode(mode):
    if next(count) == 0:
#         im = Image.open("malo21st.png")
        st.set_page_config(
            page_title="福岡県の交通事故",
#             page_icon=im,
            layout=mode,
        )

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
