# code
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(1,5,11)
y=x**2

fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
#this can create a x label for axes1
axes1.set_xlabel("this is X label")
#this can create a y label for axes1
axes1.set_ylabel("this is Y label")
#this can create a title for axes1
axes1.set_title("this is title")

axes2.plot(y,x)
#this can create a x label for axes2
axes2.set_xlabel("this is X label")
#this can create a y label for axes2
axes2.set_ylabel("this is Y label")
#this can create a title label for axes2
axes2.set_title("this is title")

plt.show()