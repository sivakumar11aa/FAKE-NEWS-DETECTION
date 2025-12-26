import streamlit as st
import joblib

vec=joblib.load('vectorizer.jb')
lr=joblib.load('lr_model.jb')

st.title("Fake News Detection")
st.write("Enter a news article to check if it's fake or real:")

new_input=st.text_area("news article:")

if st.button("check news"):
    if new_input.strip():
        transformed_input=vec.transform([new_input])
        prediction=lr.predict(transformed_input)
        if prediction[0]==1:
            st.success("The news article is Real.")
        else:
            st.error("The news article is Fake.")
    else:
        st.warning("Please enter a news article.")