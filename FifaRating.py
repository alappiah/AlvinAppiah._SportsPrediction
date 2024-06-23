import numpy as np
import pandas as pd
import streamlit as st 
#from sklearn import preprocessing
import pickle

with open('best_performing_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
def main():
    st.title("Fifa Rating Predictor")
    html_temp = """
    <div style="background:#296EB4 ;padding:10px">
        <h2 style="color:white; text-align:center;">Fifa Rating Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    movement_reactions = st.text_input("Movement Reaction","0") 
    potential = st.text_input("Potential","0") 
    passing = st.text_input("Passing","0") 
    wage = st.text_input("Wage (euros)","0") 
    mentality_composure = st.text_input("Mentality Composure","0") 
    value = st.text_input("Value (euros)","0") 
    dribbling = st.text_input("Dribbling","0") 
    attack_shot_passing = st.text_input("Attacking Shot Passing","0")
    mentality_vision = st.text_input("Mentality Vision","0")
    st.button("Predict")
if __name__=='__main__': 
    main()
