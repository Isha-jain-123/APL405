"""
Mohr circle in 3D.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16


class mohr():
  def plot_mohr3d(self, S):
    """Plot 3D Mohr circles."""
    ''' This method "plot_mohr3d()" definition should evaluate the principal stress components from any arbitrary stress tensor(S).
        Then, calculate major, minor and intermediate radius of Mohr's circle.'''

    def eigenval(M):
      w = eigvalsh(M)
      a = np.sort(w)
      return a

    y = eigenval(S)
    # print(y)
    a1 = y[2];
    a2 = y[1];
    a3 = y[0]
    R_maj = (a1 - a3) / 2
    cent_maj = (a1 + a3) / 2

    R_min = (a2 - a3) / 2
    cent_min = (a2 + a3) / 2

    R_mid = (a1 - a2) / 2
    cent_mid = (a1 + a2) / 2

    figure, axes = plt.subplots()
    axes.set(xlim=(-200, 200), ylim=(-200, 200))
    circle1 = plt.Circle((cent_maj, 0), R_maj, fill=False)
    axes.set_aspect('equal')
    axes.add_artist(circle1)
    circle2 = plt.Circle((cent_mid, 0), R_mid, fill=False)
    axes.add_artist(circle2)
    circle3 = plt.Circle((cent_min, 0), R_min, fill=False)
    axes.add_artist(circle3)
    return R_maj, R_min, R_mid


# You can use this main file to run your code

S = np.array([
  [90, 0, 95],
  [0, 96, 0],
  [95, 0, -50]])

plt.figure()
model = mohr()
R_maj, R_min, R_mid = model.plot_mohr3d(S)
print(R_maj, R_min, R_mid)
plt.show()


