import streamlit as st
import pickle
model=pickle.load(open("job_model.pkl","rb"))
vectorizer=pickle.load(open("vectorizer.pkl","rb"))
st.title("AI Job Role Predictor")
skills=st.text_area("Enter your skills","python tensorflow deep learning")
if st.button("Predict Job Role"):
    skills_vector=vectorizer.transform([skills])
    prediction=model.predict(skills_vector)
    st.success(f"Predicted Job ROLE:{prediction[0]}")