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

while uzak <= 20 :
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
print("Final absoloute velocity of the sphere is : {} m/s".format(V_abs))
print("Final height of the sphere is : {} meters".format(yuks))

energy = (0.5 * m * V_abs * V_abs) + (m*g*yuks)
print("final energy when sphere hits by the 20 meter of distance : {} Joule.".format(energy))





    
    