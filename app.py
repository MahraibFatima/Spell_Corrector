import streamlit as st

st.title('Spell Checker')

text = st.text_area("Enter Text:", value='', height=None, max_chars=None, key=None)

if st.button('Check Spelling'):
    st.balloons()