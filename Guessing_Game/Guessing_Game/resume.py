import streamlit as st

st.title("Welcome")
st.write("Hello welcome to my project")

name = st.text_input("Enter your name")
st.write(f"Welcome(name)")
btn =st.button("click me")
if btn:
    st.write("hi how r u")

st.title("My Resume")
Dict={'institution name':['abc school','kg college'],
      'year':[2024,2028],
      'marks':[90,80]}
st.dataframe(Dict)
skills=["python","java"]
for skills in skills:
    st.write(f"-{skills}")
    