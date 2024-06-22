import numpy as np
import pandas as pd
import streamlit as st 
#from sklearn import preprocessing
import pickle

def main():
    st.title("Fifa Rating Preidictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
        <h2 style="color:white; text-align:center;">Fifa Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

if __name__=='__main__': 
    main()
