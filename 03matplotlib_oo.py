# code
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig=plt.figure()
axes= fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel("this is X label")
axes.set_ylabel("this is Y label")
axes.set_title("this is Title")
plt.show()
