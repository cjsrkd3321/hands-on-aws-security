import streamlit as st
from utils.db import query_execute


def sidebar():
    with st.sidebar:
        if st.button("Clear Cache", type="primary", use_container_width=True):
            # https://steampipe.io/docs/guides/caching#client-cache-commands
            query_execute("select from steampipe_internal.meta_cache('clear')")
