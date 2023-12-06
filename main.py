import math
import numpy as np
import matplotlib.pyplot as plt

print("# FIND GRAVITY WITH SIMPLE PENDULUM #")

T = []
L = []

#input T
pTime = 0
print("##Enter values of L")
while pTime<6:
    getL = float(input("Enter the values of L(cm) : "))
    calculateL = getL/100
    L.append(calculateL)
    pTime+=1

pTime=0
print("##Enter the values of T")
while pTime<6:
    getT = float(input("Enter the values of T(s) : "))
    realT = getT/25
    calculateT = pow(realT, 2)
    T.append(calculateT)
    pTime += 1

print("-------------------------------------------------")

print("Measurements of Length(m) =",L)
print("Measurements of Time(s^2) =",T)

print("-------------------------------------------------")

#calculate G

x1 = sum(L)/6
y1 = sum(T)/6
pi2 = pow(math.pi,2)

g = (pi2*4)*(x1/y1)
print("G =",g,"m/s^2")

#draw graph using data
plt.plot(L,T, marker="o")
plt.title("Pendulum Experiment")
plt.xlabel("Length(m)")
plt.ylabel("Time(s^2)")
plt.show()
