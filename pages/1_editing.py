import streamlit as st
import pandas as pd
st.set_page_config(page_icon=":pencil:")
st.sidebar.title("sidebar")
st.sidebar.write("python code here")
s_i = st.sidebar.text_input("")
page1, page2, page3 = st.tabs(["page1", "page2", "page3"])
with page1:
    st.text_area("add", key="fine")
with page2:
    st.text_area("add more", key="fin")
with page3:
    st.text_area("add even more", key="fi")
if s_i:
    st.code(s_i, language="python")
st.divider()
df = pd.DataFrame({
    "a": ["", "", ""],
    "b": ["", "", ""],
    "c": ["", "", ""],
    "d": ["", "", ""]
})
e_df = st.data_editor(df)
