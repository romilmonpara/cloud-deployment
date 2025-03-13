import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Cloud App")
st.write(" A Simple Dataframe : ")

df = pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])
st.dataframe(df)

# when we use panda = DataFrame
# when we use streamlit = dataframe