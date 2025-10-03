"""
Demonstrates convergence of a sequence: a_n = 1/n
"""
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 51)
a_n = 1 / n

plt.plot(n, a_n, marker='o')
plt.title('Convergence of a_n = 1/n')
plt.xlabel('n')
plt.ylabel('a_n')
plt.grid(True)
plt.show()
