import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
from streamlit_folium import folium_static
import folium

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
    # map
    map_str = load_map_html("acc_map.html")
    components.html(map_str, height=600)
    # detail info
    pos_dic = load_pos_data("pos_idx.json")
    df = load_data("fuk_accidents.ftr")
    col1, col2 = st.columns((1, 1))
    with col1:
        pos_index = st.text_input("位置番号")
    with col2:
        st.write("　"); st.write("　");
        push_button = st.button('照会')
    if push_button:
        st.header('詳細情報')
        # table
        df_map = df[df.index.isin(pos_dic[pos_index])]
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

        folium_static(pos_map)
