# code
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig,axes = plt.subplots(nrows=1,ncols=2)
for current_ax in axes:
    current_ax.plot(x,y)
plt.show()