import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

ax.set_xlabel("time (s)")
ax.set_ylabel("height (m)")
ax.set_title("a wave")
ax.grid(alpha=0.3)

fig.savefig("wave.png")