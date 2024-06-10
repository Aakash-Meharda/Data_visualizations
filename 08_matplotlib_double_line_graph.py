import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig = plt.figure()

ax=fig.add_axes([0.20,0.20,0.90,0.90])
ax.plot(x**2,y,label='x squared')
ax.plot(x**3,y,label='x cubed')
ax.legend()
plt.show()