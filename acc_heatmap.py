import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

weekdays = ['月', '火', '水', '木', '金', '土', '日']
hours = list(range(0, 23 + 1))
severity = ['負傷', '死亡']
years = [2016, 2017, 2018, 2019, 2020]

@st.cache
def load_data(feather_file):
    return pd.read_feather(feather_file)

def heatmap(df, weekdays):
    if len(df):
        fig = px.imshow(pd.crosstab(df['発生曜日'], df['発生時']).reindex(index=weekdays))
    else:
        fig = px.bar()
        fig.add_annotation(font=dict(size=36), showarrow=False, text="表示するデータがありません。")
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)
    return fig

df = load_data("fuk_accidents.ftr")

def app():
    # sidebar
    select_days = st.sidebar.multiselect("曜日", weekdays, default=weekdays)
    start_hour, end_hour = st.sidebar.select_slider("時間帯", options=hours, value=(0, 23))
    select_hours = list(range(start_hour, end_hour + 1))
    select_severity = st.sidebar.multiselect("事故内容", severity, default=severity)
    select_years = st.sidebar.multiselect("発生年", years, default=years)

    # data抽出
    df_hm = df[
                df["発生曜日"].isin(select_days) &
                df["発生時"].isin(select_hours) &
                df["事故内容"].isin(select_severity) &
                df["発生年"].isin(select_years)
            ]

    #body
    st.plotly_chart(
        heatmap(df_hm, select_days)
    )
    if len(df_hm):
        st.dataframe(
            pd.crosstab(df_hm['発生曜日'], df_hm['発生時'], margins=True, 
                    margins_name='計').reindex(index=select_days+["計"])
        )
    else:
        st.error('抽出条件を設定し直して下さい。')
