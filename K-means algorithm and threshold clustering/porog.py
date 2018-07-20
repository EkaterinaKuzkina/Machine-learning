import matplotlib.pyplot as plt
import os
import numpy as np
import random
import math
import pylab

def evklid(x, y):
#    print(x)
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    
n = 1000
s=40
klaster1=klaster2=klaster3=klaster4=klaster5=klaster6=np.empty([0,2])
a=np.empty([n,2])
standart = np.empty([1,2])

#Заполняем общую выборку
h=0
random.seed(5000)
for i in range(n):
    if h == 0:
        a[i][0] = random.randint(10,50)
        a[i][1] = random.randint(10,30)
        h+=1
    elif h == 1:
        a[i][0] = random.randint(10,50)
        a[i][1] = random.randint(40,70)
        h+=1
    elif h == 2:
        a[i][0] = random.randint(70,100)
        a[i][1] = random.randint(40,70)
        h+=1
    elif h == 3:
        a[i][0] = random.randint(70,100)
        a[i][1] = random.randint(10,30)
        h=0
t = np.zeros([n,1])       
standart[0] = a[0]

for i in range(len(a)):
    minlen = 10000
    temp_klast = 200
    for j in range(len(standart)):
        if (evklid(a[i],standart[j]) < s) and (evklid(a[i],standart[j]) < minlen):
            minlen = evklid(a[i],standart[j])
            temp_klast = j
    if temp_klast==200:
        standart = np.append(standart, [a[i]], axis=0)
        t[i] = len(standart)-1
    else:
         t[i] = temp_klast
#print(standart) 
#print(t)
print(len(standart))           
plt.subplot(1,1,1)
for i in range(len(t)):
    if t[i]==0:
        plt.plot(a[i][0], a[i][1], "o", color='m')
    elif t[i]==1:
        plt.plot(a[i][0], a[i][1], "o", color='y')
    elif t[i]==2:
        plt.plot(a[i][0], a[i][1], "o", color='g')
    else:
        plt.plot(a[i][0], a[i][1], "o", color='b')
#for i in range(len(klaster3)):
#     plt.plot(klaster3[i][0], klaster3[i][1], "o", color='r')
#for i in range(len(klaster4)):
#     plt.plot(klaster4[i][0], klaster4[i][1], "o", color='g')
plt.grid(True)
plt.ylabel('Y')
plt.xlabel('X')
plt.title ("Простая форма. Пороговое расстояние = 40 ")
plt.show()