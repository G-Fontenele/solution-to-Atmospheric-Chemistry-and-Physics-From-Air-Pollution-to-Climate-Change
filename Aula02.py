# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:26:43 2021

@author: gonca
"""

import numpy as np

R= 83144.7 # cm^3mbarK^-1mol^-1
avogrado = 6.022*10**23
RHs = [50,60,70,80,90,95,99]

def pH2O(T, RH):
    a = (T-373.15)/T
    b = np.exp(13.3185*a-(1.97*(a**2))-(0.6445*(a**3))-(0.1299*(a**4)))
    p0 = 1013.25*b
    p =  (RH*p0)/100
    return p
    
def concent(T, Mi, mixingRatio, P):
    c = (Mi*mixingRatio*P)/(8.314*T)
    return c

def mixingRatio(T, Mi, concentration, P): # P in Pascal
    concentration = concentration*10**-6
    mr = (8.314*T*concentration)/(P*Mi)
    return mr
    
    
def N(p, T):
    n = (p*avogrado)/(R*T)
    return n

print ('--------------------------------------------------------')

print ('Exercicio 1')
for RH in RHs:
    p = pH2O(298, RH)
    n = N(p, 298)
    mr = mixingRatio(298,18,18*n,101325)
    print('Caso ' +str(RHs.index(RH)+1))
    print('pH2O '+str(p))
    print('N '+str(n)+ ' cm^-3')
    print('Mixing Ratio '+str(mr)+ ' ppm')

    
print ('--------------------------------------------------------')

    
print('Exercício 2')
print('Concentração em ug*m^-3')
print(concent(298,44,0.311,101325))
print ('--------------------------------------------------------')

print('Exercício 3')
print('Mixing Ratio')
print(mixingRatio(298,17.008,10**6,101325))
print ('--------------------------------------------------------')

print('Exercício 4')
print('Mixing Ratio')
print('De ' +str(mixingRatio(298,62.14,250*10**3,101325)) + ' ppm até ' +str(mixingRatio(298,62.14,500*10**3,101325))+ ' ppm')
print ('--------------------------------------------------------')


