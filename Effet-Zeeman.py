# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:34:27 2021

@author: Saadia Bayou
"""



K=4.67*1e-13
l1=6301.5
l2=6302.5

g2=1.67
g1=2.50

dlB1=(0.25/2)
dlB2=(0.20/2)

def champ_mag(g,l,dlB):
    return dlB/(K*g*(l**2))

B1=champ_mag(g1,l1,dlB1)

B2=champ_mag(g2,l2,dlB2)

print("B1 = ",B1)

print("B2 = ",B2)

