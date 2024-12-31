import pandas as pd
import streamlit as st
from utils.db import engine
from pages.commons.sidebar import sidebar


st.set_page_config(page_title="직접쿼리", page_icon="🔍", layout="wide")
sidebar()

st.title("직접 쿼리 하기")
st.link_button("플러그인 살펴보기", "https://hub.steampipe.io/")

with st.form("query"):
    query = st.text_area(
        label="Editor",
        placeholder="쿼리를 입력해주세요...",
        value="SELECT * FROM aws_ec2_instance",
    )
    submitted = st.form_submit_button("실행")

if submitted and query:
    with st.spinner("쿼리 중..."):
        try:
            d = pd.read_sql_query(query, con=engine)
        except Exception as e:
            st.exception(e)
        else:
            st.dataframe(d, use_container_width=True)
else:
    st.error("쿼리를 입력 후 실행해주세요.", icon="🚨")
