# https://docs.streamlit.io/develop/api-reference/configuration/config.toml#view-all-configuration-options
import streamlit as st
import pandas as pd
from utils.db import engine
from pages.commons.sidebar import sidebar


st.set_page_config(
    page_title="AWS 보안 대시보드",
    page_icon=":shield:",
    layout="wide",
    initial_sidebar_state="expanded",
)
sidebar()

st.title("STEAMPIPE 설정 대시보드")

st.header("사용 가능 연결 현황")
with st.spinner("쿼리 중..."):
    d = pd.read_sql_query(
        "SELECT name, state, type, connections, import_schema, error FROM steampipe_connection",
        con=engine,
    )
st.dataframe(d, use_container_width=True)

st.header("서버현황")
with st.spinner("쿼리 중..."):
    d = pd.read_sql_query(
        "SELECT start_time, steampipe_version, fdw_version, cache_max_ttl, cache_enabled FROM steampipe_server_settings",
        con=engine,
    )
st.dataframe(d, use_container_width=True)
