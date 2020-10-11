import numpy as np
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
import os

plt.rcParams['mathtext.fontset'] = 'cm'
font = {'family' : 'serif', 
        'weight' : 'normal', 
        'size': 20}
plt.rc('font', **font)
plt.rc("lines", lw=2)

p_phi = 1.7
p_psi = 1
I_1 = 1
Mgh = 0.3
n = 1000
theta_min = 0
yrange = (-5, 40)

def V(theta):
    return (p_phi - p_psi * cos(theta)) ** 2 / (2 * I_1 * sin(theta)**2) + Mgh * cos(theta)
    
theta = np.linspace(0, pi - theta_min, n)
i0 = np.argmin(V(theta))


fig, ax = plt.subplots(figsize = (5, 5.5))

ax.plot(theta, V(theta))
ax.plot([theta[i0], theta[i0]], [yrange[0], 1.2 * V(theta[i0])], "--k", lw=1)
ax.text(theta[i0], V(theta[i0]), "$\\theta_0$", verticalalignment="bottom")

ax.set_xlabel("$\\theta$")
ax.set_ylabel("$V(\\theta)$")
ax.set_ylim(*yrange)


plt.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
plt.savefig(here + "/exercise_3_plot.pdf")
# plt.show()
