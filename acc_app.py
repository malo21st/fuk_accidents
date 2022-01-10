import streamlit as st
import acc_heatmap, acc_map #, acc_table
from multipage import MultiPage
# from PIL import Image

st.session_state.times = 0

def set_mode(mode):
#     im = Image.open("malo21st.png")
    if not st.session_state.times:
        st.set_page_config(
            page_title="福岡県の交通事故",
            layout=mode,
#             page_icon=im,
        )
    else:
        st.session_state.times += 1

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
