import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12,8))

plt.plot([1,2,3,4,5])

st.pyplot(fig)