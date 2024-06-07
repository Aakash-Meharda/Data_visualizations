import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig,axes = plt.subplots(nrows=1,ncols=3)
axes[0].plot(x,y)
axes[1].plot(y,x)
axes[2].plot(x,y)
plt.show()