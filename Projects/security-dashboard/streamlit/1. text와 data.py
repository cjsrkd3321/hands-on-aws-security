# https://docs.streamlit.io/develop/api-reference/text
# https://docs.streamlit.io/develop/api-reference/data
import random
import streamlit as st
import pandas as pd


st.title("대시보드", anchor="title")
st.header("안녕하세요.")

st.text("HELLO!")

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [
            [random.randint(0, 5000) for _ in range(30)] for _ in range(3)
        ],
    }
)

st.dataframe(df)
st.table(df)
