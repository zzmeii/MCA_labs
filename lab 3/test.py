import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 60, 0.1)


def f(x):
    return np.sin(x / 10) * 10


y = [f(i) for i in x]
plt.plot(x,y)
plt.show()