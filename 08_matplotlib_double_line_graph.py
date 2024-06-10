import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig = plt.figure()

ax=fig.add_axes([1,1,2,2])
ax.plot(x,y**2,label='y squared')
ax.plot(x**2,y,label='x squared')
ax.legend()
plt.show()