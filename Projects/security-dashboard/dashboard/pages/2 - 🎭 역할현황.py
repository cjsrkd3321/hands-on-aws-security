import pandas as pd
import streamlit as st
from utils.db import engine
from pages.commons.sidebar import sidebar


st.set_page_config(page_title="역할현황", page_icon="🎭", layout="wide")
sidebar()

st.title("IAM 역할 대시보드")
st.header("미사용 역할 현황")
with st.spinner("쿼리 중..."):
    d = pd.read_sql_query(
        f"SELECT account_id, path, name, role_id, role_last_used_date FROM aws_iam_role WHERE role_last_used_date IS NULL",
        con=engine,
    )
st.dataframe(d, use_container_width=True)
