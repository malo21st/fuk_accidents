import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
from streamlit_folium import folium_static
import folium
import numpy as np
import itertools
# import pyperclip

pos_index = ""

@st.cache
def load_map_html(html_file):
    with open(html_file, mode="r") as f:
        return f.read()

@st.cache
def load_pos_data(pos_file):
    with open(pos_file, mode="r") as f:
        return json.load(f)

@st.cache
def load_data(acc_file):
    return pd.read_feather(acc_file)

#wrap all your code in this method and you should be done
def app():
    global pos_index
    # map
    map_str = load_map_html("acc_map.html")
    components.html(map_str, height=600)
    # detail info
    df = load_data("fuk_accidents.ftr")
    pos_dic = load_pos_data("pos_idx.json")
    col1, col2, col3, col4, col5 = st.columns((5, 1, 1, 1, 2))
    with col1:
#         element = st.info(pos_index)
        element = st.text_input(value=pos_index)
    with col2:
        # st.write("　"); st.write("　");
        add_button = st.button('追加')
    with col3:
        # st.write("　"); st.write("　");
        inquiry_button = st.button('照会')
    with col4:
        clear_button = st.button('消去')
    with col5:
        st.empty()

#     if add_button:
#         pos_index += pyperclip.paste() + " "
#         element.info(pos_index)

    if clear_button:
        pos_index = ""
        element.info(pos_index)

    if inquiry_button:
        st.header('詳細情報')
        df_map = pd.DataFrame()
        try:
            index_lst = list(itertools.chain.from_iterable([pos_dic[p] for p in set(pos_index.split())]))
            df_map = df[df.index.isin(index_lst)]
        except:
            st.warning("位置コードが正しくありません。")

        if len(df_map):
            # table
            df_map.reset_index(drop=True, inplace=True)
            df_map.index = np.arange(1, len(df_map)+1)
            st.dataframe(df_map)
            # map
            pos_lat = df_map["発生場所緯度"] 
            pos_lon = df_map["発生場所経度"] 
            center= [(max(pos_lat)+min(pos_lat)) / 2, (max(pos_lon)+min(pos_lon)) / 2]

            pos_map = folium.Map(location=center, zoom_start=18)

            for _, row in df_map.iterrows():
                folium.CircleMarker(
                    location = [row["発生場所緯度"], row["発生場所経度"]],
                    tooltip = row["No."],
                    radius=2,
                    color="red",
                    fill=True,
                    fill_color="red",
                ).add_to(pos_map)
                
            pos_map.fit_bounds([(min(pos_lat), min(pos_lon)), (max(pos_lat), max(pos_lon))])

            folium_static(pos_map)
