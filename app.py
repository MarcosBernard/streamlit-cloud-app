import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,20,100)
y = np.sin(x)


plt.figure(figsize=(12,8))
plt.plot(x,y,'-')
plt.show()