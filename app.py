import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

#create your figure and get the figure object returned
fig = plt.figure()
plt.plot([1,2,3,4,5])

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600) 