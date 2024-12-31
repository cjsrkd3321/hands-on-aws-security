import streamlit as st
import pandas as pd
from utils.db import engine, clear_cache


st.set_page_config(
    page_title="클라우드 계정 정보",
    page_icon="🦈",
    layout="wide",
)

with st.sidebar:
    if st.button(
        "캐시 클리어",
        type="primary",
        use_container_width=True,
    ):
        clear_cache()

st.title("클라우드 계정 정보")
st.header("AWS 계정 정보")

with st.spinner("쿼리 중..."):
    df = pd.read_sql_query(
        sql="SELECT account_id, account_aliases, organization_arn FROM aws_account",
        con=engine,
    )
    st.dataframe(df, use_container_width=True)
