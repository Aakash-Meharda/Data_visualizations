import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

plt.plot(x,y)
plt.xlabel("this is X label")
plt.ylabel("this is Y label")
plt.title("tut1 is title")
plt.show()
