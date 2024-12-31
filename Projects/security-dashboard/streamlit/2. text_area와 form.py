# https://docs.streamlit.io/develop/api-reference/widgets/st.text_area
# docs.streamlit.io/develop/api-reference/execution-flow#group-multiple-widgets
import streamlit as st


txt = st.text_area(
    label="쿼리 입력창",
    placeholder="쿼리를 입력해주세요.",
    value="SELECT * FROM aws_vpc",
)

st.text(f"You wrote {len(txt)} characters.")

with st.form("query"):
    submitted = st.form_submit_button("쿼리하기")

st.write(submitted)

with st.form("text_area_with_form"):
    txt = st.text_area(
        label="쿼리 입력창",
        placeholder="쿼리를 입력해주세요.",
        value="SELECT * FROM aws_vpc",
    )
    submitted = st.form_submit_button("쿼리하기")
    if txt and submitted:
        st.text(f"{txt}, {submitted}")
