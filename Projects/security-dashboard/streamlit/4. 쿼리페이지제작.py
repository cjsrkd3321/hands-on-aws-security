import streamlit as st
import pandas as pd
from utils.db import engine, clear_cache


with st.sidebar:
    if st.button(
        "캐시 클리어",
        type="primary",
        use_container_width=True,
    ):
        clear_cache()

st.title("쿼리페이지")

with st.form("query"):
    query_str = st.text_area(
        label="쿼리 입력창",
        placeholder="쿼리를 입력해주세요.",
        value="SELECT * FROM aws_vpc",
    )
    submitted = st.form_submit_button("쿼리하기")

if query_str and submitted:
    with st.spinner("쿼리 중..."):
        try:
            df = pd.read_sql_query(sql=query_str, con=engine)
        except Exception as e:
            st.exception(e)
        else:
            st.dataframe(df)
else:
    st.error("쿼리를 입력해주세요!", icon="🚨")
