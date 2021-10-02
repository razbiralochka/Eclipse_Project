import math as m
import numpy as np
import matplotlib.pyplot as plt
E=7.4
C=2500

def U(C):
    if C < 3600:
        return 7.4*(1-m.exp(-0.001*C))
    else:
        return 7.4
t=0
h=10


T=[]
Cap=[]

while C < 3600:
    T.append(t)
    Cap.append(C)
    C = C + ((E-U(C))/10) * h
    t = t + h


while C > 2500:
    T.append(t)
    Cap.append(C)
    C = C + (((E-U(C))/10)-0.25) * h
    t = t + h

while C < 3600:
    T.append(t)
    Cap.append(C)
    C = C + ((E-U(C))/10) * h
    t = t + h


while C > 2500:
    T.append(t)
    Cap.append(C)
    C = C + (((E-U(C))/10)-0.25) * h
    t = t + h
        

plt.plot(T,Cap)