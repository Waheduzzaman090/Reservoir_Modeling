# -*- coding: utf-8 -*-
"""
Created on 6/3/2024

@author: % Md. Waheduzzaman Nouman
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
#def randfield(nx, dx, lx, Ctype, dimen, sigma2, mu, ang = [0,0,0]):

    
nx = [40,40,4]
ang = [0,0,0]
dx = [1,1,1]
lx = [4,20,1]
sigma2 = 0.02
mu = .17

ntot = np.array(nx).prod()
ang1 = ang[0]
ang2 = ang[1]
ang3 = ang[2]

x = range(int(-nx[0]/2)*dx[0],int(nx[0]/2)*dx[0],dx[0])
y = range(int(-nx[1]/2)*dx[1],int(nx[1]/2)*dx[1],dx[1])
z = range(int(-nx[2]/2)*dx[2],int(nx[2]/2)*dx[2],dx[2])

[X,Y,Z]=np.meshgrid(x,y,z)
a = [[math.cos(ang1), math.sin(ang1), 0],[-math.sin(ang1), math.cos(ang1), 0], [0,         0,         1]]
b = [ [math.cos(ang2), 0,         math.sin(ang2)], [0,         1,         0],[-math.sin(ang2), 0,         math.cos(ang2)]] 
c = [[ 1,         0,         0       ] ,[0,         math.cos(ang3), math.sin(ang3)], [0,        -math.sin(ang3), math.cos(ang3)]]
Rotmat =   np.matmul(np.matmul(a,b),c)
  
X2= Rotmat[0,0]*X + Rotmat[0,1]*Y + Rotmat[0,2]*Z
Y2= Rotmat[1,0]*X + Rotmat[1,1]*Y + Rotmat[1,2]*Z
Z2= Rotmat[2,0]*X + Rotmat[2,1]*Y + Rotmat[2,2]*Z


   
H = np.sqrt((X2/lx[0])**2+(Y2/lx[1])**2+(Z2/lx[2])**2);

RYY=np.exp(-abs(H))*sigma2
#RYY = np.exp(-H**2)*sigma2
SYY = np.fft.fftn(np.fft.fftshift(RYY))/ntot
SYY=abs(SYY)
SYY[0,0,0] = 0


a = nx[1]
b = nx[0]
c = nx[2]
ran = np.multiply(np.sqrt(SYY),np.exp(1j*np.angle(np.fft.fftn(np.random.rand(a,b,c)))))
ran  = np.fft.ifftn(ran*ntot).real 

ran = ran + mu
ran = np.clip(ran, 0.001,1000)

slice_2d = ran[:, :,0]


print(np.mean(ran),np.var(ran))
poro = 100*ran


perm = -2.03E-07*poro**5+2.55E-05*poro**4-1.04E-03*poro**3 +8.91E-03*poro**2+3.58E-01*poro**1-3.21E+00
perm = 10**perm+1
print(np.max(perm),np.min(perm))


vmin, vmax =np.min(poro/100), np.max(poro/100) # For example purposes, set your own min and max values

norm = Normalize(vmin=vmin, vmax=vmax)
img = plt.imshow(slice_2d, cmap='viridis', norm=norm)
cbar = plt.colorbar(img, label='Value')


plt.title('2D Slice of Correlated 3D Field')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Show the plot
plt.show()
poro = ran
i = 0
data = np.zeros((nx[0]*nx[1]*nx[2],2))
for z in np.arange(nx[2]):
    for x in np.arange(nx[1]):
        for y in np.arange(nx[0]):
            data[i,0] = poro[x,y,z]
            data[i,1] = perm[x,y,z]
            i += 1
np.savetxt("data.csv",data,   delimiter = ",")