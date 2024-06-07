import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

plt.subplot(1,2,1)
# it tkae irst ncols , nrows , plotno
plt.plot(x,y,"g")

plt.subplot(1,2,2)
plt.plot(y,x,"r")
plt.show()
