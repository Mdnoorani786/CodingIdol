#python 3.7.1
import pandas as pd
import matplotlib.pyplot as plt
a=["python","java","C++","PHP"]
b=[73,79,33,29]
c=["b","g","y","brown"]
plt.title("Best language",fontsize=10)
plt.xlabel("language")
plt.ylabel("demand ")
plt.bar(a,b,width=0.6,edgecolor="r",color=c)
plt.show()