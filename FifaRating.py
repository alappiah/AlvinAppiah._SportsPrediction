import numpy as np
import pandas as pd
import streamlit as st 
import pickle
import xgboost

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

    movement_reactions = st.text_input("Movement Reaction","80") 
    potential = st.text_input("Potential","89") 
    passing = st.text_input("Passing","80") 
    wage = st.text_input("Wage (euros)","100000") 
    mentality_composure = st.text_input("Mentality Composure","70") 
    value = st.text_input("Value (euros)","200000") 
    dribbling = st.text_input("Dribbling","82") 
    attack_shot_passing = st.text_input("Attacking Shot Passing","80")
    mentality_vision = st.text_input("Mentality Vision","90")

    # Prediction button
    if st.button("Predict"):
        # Convert inputs to float and create feature array
        try:
            features = np.array([
                int(movement_reactions),
                int(potential),
                int(passing),
                int(wage),
                int(mentality_composure),
                int(value),
                int(dribbling),
                int(attack_shot_passing),
                float(mentality_vision)
            ]).reshape(1, -1)
            
            # Make prediction
            prediction = model.predict(features)
            
            # Display the result
            st.success(f'The predicted Fifa Rating is: {prediction[0]:.2f}')
        
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")
            
if __name__=='__main__': 
    main()
