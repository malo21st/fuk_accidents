import streamlit as st
import pandas as pd
import plotly.express as px


weekdays = ['月', '火', '水', '木', '金', '土', '日']
hours = [h for h in range(0, 23 + 1)]
severity = ['負傷', '死亡']
years = [2016, 2017, 2018, 2019, 2020]

@st.cache
def load_data():
    return pd.read_feather("fuk_accidents.ftr")

def heatmap(df, weekdays):
    if len(df):
        fig = px.imshow(pd.crosstab(df['発生曜日'], df['発生時']).reindex(index=weekdays))
    else:
        fig = px.bar()
        fig.add_annotation(font=dict(size=36), showarrow=False, text="NO DATA")
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)
    return fig

df = load_data()

#body
st.header("福岡県の交通事故")

select_days = st.sidebar.multiselect("曜日", weekdays, default=weekdays)

start_hour, end_hour = st.sidebar.select_slider(
    "時間帯", 
    options=hours,
    value=(0, 23),
    )
select_hours = [h for h in range(start_hour, end_hour + 1)]

select_severity = st.sidebar.multiselect("事故内容", severity, default=severity)
select_years = st.sidebar.multiselect("発生年", years, default=years)

df_hm = df[
    df["発生曜日"].isin(select_days) &
    df["発生時"].isin(select_hours) &
    df["事故内容"].isin(select_severity) &
    df["発生年"].isin(select_years)
]

st.write(
    heatmap(df_hm, select_days)
)