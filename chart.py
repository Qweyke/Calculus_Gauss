import matplotlib.pyplot as plt
import numpy as np

x = [- 3, - 2, -1, 0, 1, 2, 3]
y = [9, 4, 1, 0, 1, 4, 9]

fig, ax = plt.subplots()

ax.plot(x, y, color='red', ls='--', marker='^', label='y = x^2')

ax.set_title('parabola')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.grid(True)

plt.show()

