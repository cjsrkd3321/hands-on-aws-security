import pandas as pd
import streamlit as st
from utils.db import engine
from pages.commons.sidebar import sidebar


st.set_page_config(page_title="계정현황", page_icon="👤", layout="wide")
sidebar()

st.title("계정 대시보드")
st.header("AWS 계정 현황")
with st.spinner("쿼리 중..."):
    d = pd.read_sql_query(
        "SELECT account_id, account_aliases, organization_arn, organization_id, organization_master_account_id FROM aws_account",
        con=engine,
    )
st.dataframe(d, use_container_width=True)
