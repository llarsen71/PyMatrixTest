import pylab as plt
import numpy as np
from math import pi, cos, sin

def ortho(deg):
  a = deg*pi/180
  return np.matrix([[cos(a),sin(a)],[-sin(a),cos(a)]])

A = np.matrix([[10,0],[0,0.01]])

d = []
o = []
la = []
ld = []
for deg in range(0,361):
  P = ortho(deg)
  Ar = P*A*P.T
  cosa = float(Ar[0,:] * Ar[1,:].T)/(float(Ar[0,:]*Ar[0,:].T)**0.5*float(Ar[1,:]*Ar[1,:].T)**0.5)
  lena = (float(Ar[0,:]*Ar[0,:].T)**0.5+float(Ar[1,:]*Ar[1,:].T)**0.5)/2
  lend = (float(Ar[0,:]*Ar[0,:].T)**0.5-float(Ar[1,:]*Ar[1,:].T)**0.5)/2
  d.append(deg)
  o.append(cosa)
  la.append(lena)
  ld.append(lend)
  
plt.plot(d,o)
plt.figure()
plt.plot(d,la)
plt.figure()
plt.plot(d,ld)
plt.show()