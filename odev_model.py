# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:48:04 2023

@author: Mehmet Akif ERDAS
"""
import math
import matplotlib.pyplot as plt

yuks = 1.5 # height
uzak = 0 #distance from start
V_int = 112.64 #initial velocity / calculated by curve fitting that can be found in the zip file.
a_sx = 0 #lateral acceleration
t_sure = 0 # time model
t= 0.01 # time interval/period
A_r = 0.0000287433 #projected area of the sphere
V_sx = V_int - (a_sx * t) #lateral velocity
ro_hava = 1.228 #kg/m3 air density
m = 0.00026 #kg mass of the bullet
g= 9.80665 #gravity
c_d = 0.5142 # trial-error method 
V_sy = 0 #initial vertical speed
F_dy = 0.5 * ro_hava * c_d * A_r * V_sy * V_sy # air resistence on y axis
sayac =0

uzak_list = [] #distance data is collected in this list
V_list = [] #Velocity data is collected in this list
yuks_list = [] #height data is collected in this list

while yuks >= 0 :
    F_dx = 0.5 * ro_hava * c_d * A_r * V_sx * V_sx # air resistence on y axis
    a_sx = F_dx / m #lateral acceleration
    V_sx = V_sx - (a_sx * t) #lateral velocity
    uzak = uzak + V_sx*t #distance from start
    
    
    
    
    F_ty = m*g - F_dy #total force applied to mass on y axis
    a_sy = F_ty/m #vertical accelaration
    V_sy = V_sy + (a_sy * t) #lateral velocity
    F_dy = 0.5 * ro_hava * c_d * A_r * V_sy * V_sy #Air resistence on y axis
    
    yuks = yuks - V_sy*t #height/ fall down model
    
    euler = math.atan(F_dy/F_dx) #açı
    
    V_abs = math.sqrt((V_sy*V_sy) + (V_sx*V_sx)) #absoloute velocity
    
    V_list.append(V_abs) #restoring data to the lists
    uzak_list.append(uzak)
    yuks_list.append(yuks)
    
    
    
    
    sayac += 1 #just a control variable for myself on the program.
    t_sure = t_sure + t #continue time
    
print("total time passed (secs) : {}".format(t_sure))#print the total time passed


plt.figure() 

velocity=[108.83, 88.84, 76.41, 64.27] #average of the given velocity datas
distence=[1, 6, 11, 16]

plt.plot(uzak_list, V_list, 'r-', label = "velocity/distance curve")
plt.plot(distence,velocity,'bo',label='given velocity/distance datas')
plt.legend()
plt.show() #plot

plt.plot(uzak_list, yuks_list, 'r-')
plt.legend()
plt.title("Trajectory")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.show() #plot-trajectory


    
    