import numpy as np
from matplotlib.animation import FuncAnimation
from math import sin, cos, pi
import pylab as plt

A = np.matrix([[1,-0.01],[1,0.01]])

fig = plt.figure()

ev = []

def update(deg):
  rad = deg*pi/180
  P = np.matrix([[cos(rad),-sin(rad)],[sin(rad), cos(rad)]])
  A1 = P*A*P.T
  v = np.linalg.eig(A1)
  #print(v[0])
  #print(v[1][:,1])
  #print(A1*v[1][:,1])
  #print(deg)
  e1 = v[1][:,0]
  e2 = v[1][:,1]
  p = plt.plot([0,e1[0]], [0,e1[1]])
  plt.plot([0,e2[0]], [0,e2[1]], color = p[0].get_color())
  
ani = FuncAnimation(fig, update, interval=1000, frames=np.linspace(0,180,100))

plt.show()
