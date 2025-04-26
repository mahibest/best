import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import matplotlib.pyplot as plt
from streamlit_extras.let_it_rain import rain
home_page = st.Page("cool.py", title="Home", icon=":material/home:", default=True)
settings_page = st.Page("1_editing.py", title="edit", url_path="edit")
pg = st.navigation([home_page, settings_page])
pg.run()
st.title("hi")
st.header("best coolest thing in the world")
st.subheader("yah")
st.markdown("_yee_ **ha**")
st.write("horay")
st.caption("hehe")
st.divider()
py = """
yay = input("hi")
print(yay, " ok")
"""
st.code(py, language="python")
b = st.button("press me")
st.write(b)
b2 = st.button("no, press me")
st.write(not b2)
st.write([{"cool"}])
st.write({"cool"})
st.divider()
st.image(os.path.join(os.getcwd(), "image.png"))
st.divider()
st.subheader("boring stuff fun!!!")
df = pd.DataFrame({
    "stuff": ["yes", "yah", "yaey"],
    "more stuff": [":|", ":)", ":D"],
    "more more stuff": ["st", "u", "ff"],
    "2 much": [12345678, 546783, 53462]
})
st.dataframe(df)
st.table(df)
st.metric(label="columns", value=len(df))
st.metric(label="forgot this one", value=round(df["2 much"].mean(), 10))
s_dict = {
    "1": 12,
    "2": "3"
}
st.json(s_dict)
st.write("a:", s_dict)
st.divider()
st.subheader("charts :O")
qw = pd.DataFrame(
    np.random.randn(879, 3), 
    columns=["a", "b", "c"]
)
st.area_chart(qw)
st.bar_chart(qw)
st.line_chart(qw)
qwe = pd.DataFrame({
   "q": np.random.randn(123),
   "e": np.random.randn(123)
})
st.scatter_chart(qwe)
qwer = pd.DataFrame(
    np.random.randn(1234, 2) / [34, 34] + [23.23, 12.12],
    columns=["lat", "lon"]
)
st.map(qwer)
qwert ,qwerty = plt.subplots()
qwerty.plot(qw["a"], label="a")
qwerty.plot(qw["b"], label="b")
qwerty.plot(qw["c"], label="c")
qwerty.set_title("pyplot")
qwerty.legend()
st.pyplot(qwert)
st.divider()
with st.form(key="form"):
    st.subheader("form")
    n = st.text_input("enter something")
    q = st.text_area("same again")
    y = st.time_input("again!")
    g = st.date_input("you know the drill")
    t = st.radio("choose", ["1", "23", "78"])
    f = st.selectbox("choose again", ["34", "2", "89"])
    j = st.select_slider("choose!!!", ["90", "34", "09"])
    e = st.checkbox("click")
    d = st.checkbox("click again", value=False)
    w = st.form_submit_button()   
if w:
    st.write(n)
    st.write(q)
    st.write(y)
    st.write(g)
    st.write(t)
    st.write(f)
    st.write(j)
    st.write(e)
    st.write(d)
st.divider()
st.subheader("fun buttons")
u = st.button("want a warning")
if u:
    st.warning("warning: you asked for this")
i = st.button("want some balloons")
if i:
    st.balloons()
o = st.button("want a success")
if o:
    st.success("yay!!!!!!!!!")
v = st.button("want a notification")
if v:
    st.toast("notification: hello")
p = st.button("let it rain")
if p:
    rain(emoji="💧", font_size=50, falling_speed=5, animation_length="infinite")
st.divider()
st.subheader("Counter")
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.write(f"Counter value: {st.session_state.counter}")
def increes():
    st.session_state.counter += 1
    st.rerun()
def reeset():
    st.session_state.counter = 0
    st.rerun()
if st.button("increase"):
    increes()
if st.button("reset"):
    reeset()
st.divider()
st.subheader("parts")
if "step" not in st.session_state:
    st.session_state.step = 1
if "info" not in st.session_state:
    st.session_state.info = {}
if st.session_state.step == 1:
    st.header("part 1")
    name = st.text_input("name", value=st.session_state.info.get("name", ""))
    p = st.button("next part")
    if p:
        st.session_state.name = name
        st.session_state.step = 2
elif st.session_state.step == 2:
    st.header("part 2")
    st.write("hello", st.session_state.name)
st.divider()    
st.subheader("oooo advanced stuff")
m_v = st.slider("sét min value", 0, 50, 25)
s_v = st.slider("slider", m_v, 100, m_v)
s = st.checkbox("more")
if s:
    st.write("hi there")
    k = st.text_input("", key="asdfgh")
    st.write(k)
st.divider()
st.subheader("cache")
st.write("enter amount to see magic")
@st.cache_data(ttl=10)
def togetcash(amount):
    time.sleep(3)
    return {"$": amount, "cash": "this is cached data!"}
money = st.text_input("amount needed")
st.write("feching cash...")
data = togetcash(money)
st.write(data)
