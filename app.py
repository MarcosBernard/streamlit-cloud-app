'''
import streamlit as st
import matplotlib.pyplot as plt

#create your figure and get the figure object returned
fig = plt.figure()
plt.plot([1,2,3,4,5])

st.pyplot(fig)
'''
'''
import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components


#create your figure and get the figure object returned
fig = plt.figure()
plt.plot([1,2,3,4,5])

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
'''
#Imports for all of the code
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
import streamlit as st
from mpld3 import plugins


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

# How to set the graph size
two_subplot_fig = plt.figure(figsize=(6,6))
plt.subplot(211)
plt.plot(t1,f(t1),color='tab:blue',marker=',')
plt.plot(t2,f(t2),color='black',marker='.')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange',linestyle='--',marker='.')

st.pyplot(two_subplot_fig)
