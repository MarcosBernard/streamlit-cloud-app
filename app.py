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
'''
'''
#Imports for all of the code
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
import streamlit as st
from mpld3 import plugins
import streamlit.components.v1 as components

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

fig_html = mpld3.fig_to_html(two_subplot_fig)
components.html(fig_html, height=600)
'''
import matplotlib.pyplot as plt, mpld3
import numpy as np
from mpld3 import plugins
import streamlit.components.v1 as components
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

two_subplot_fig = plt.figure(figsize=(8,8))
plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker=',')
plt.plot(t2, f(t2), color='black', marker='.')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--', marker='.')

# Define some CSS to control our custom labels
css = '''
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
'''

for axes in two_subplot_fig.axes:
  for line in axes.get_lines():
    xy_data = line.get_xydata()
    labels = []
    for x,y in xy_data:
      html_label = f'<table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> </thead> <tbody> <tr> <th>x</th> <td>{x}</td> </tr> <tr> <th>y</th> <td>{y}</td> </tr> </tbody> </table>'
      labels.append(html_label)
    tooltip = plugins.PointHTMLTooltip(line, labels, css=css)
    plugins.connect(two_subplot_fig, tooltip)

fig_html = mpld3.fig_to_html(two_subplot_fig)
components.html(fig_html, height=850, width=850)