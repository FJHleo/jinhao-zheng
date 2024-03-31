import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

m = [10.0, 4.0, 5.0, 6.0]
miu = [0.25, 0.3, 0.2]
g = 9.82
theta = math.pi / 4

A = [
    [1.0, 0.0, 0.0, m[0]],
    [-1.0, 1.0, 0.0, m[1]],
    [0.0, -1.0, 1.0, m[2]],
    [0.0, 0.0, -1.0, m[3]],
]
b = [
    (m[0] * g * (math.sin(theta) - miu[0] * math.cos(theta))),
    (m[1] * g * (math.sin(theta) - miu[1] * math.cos(theta))),
    (m[2] * g * (math.sin(theta) - miu[2] * math.cos(theta))),
    -m[3] * g,
]

X = np.linalg.solve(A, b)
accele = X[3]
print("accelerations:", X[3])

v0 = 0
r0 = 100


def f(accele, t):
    return r0 - v0 * t - 0.5 * accele * t**2


fig, ax = plt.subplots()

ax.set_xlim(0, 40)
ax.set_ylim(-1000, 100)

t = np.linspace(0, 40, 1000)
(line,) = ax.plot(t, f(accele, t))
(point,) = ax.plot(0, 0, "o")


def animate(i):
    pos = i, f(accele, i)
    point.set_data(*pos)
    t = np.linspace(0, i, 10 * i)
    line.set_data(t, f(accele, t))


ani = FuncAnimation(
    fig, animate, frames=t.size, interval=100, blit=False, save_count=500
)

plt.show()
