import matplotlib.pyplot as plt
import os
import numpy as np
import random
import math
import pylab

def evklid(x1, y1,x2,y2,r):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)/r

def evkl(x, standart):
    splits=np.empty([0,1])
    for i in range(len(x)):
        temp = math.sqrt((x[i][0]-standart[0])**2+(x[i][1]-standart[1])**2)
        splits = np.append(splits, [[temp]], axis=0)
    return splits

def calcul_radius(x, standart):
    splits=evkl(x, standart)**2
    return math.sqrt(splits.sum()/(len(x)))

def calcul_standart(x):
    sum1 = sum2 = 0
    for i in range(len(x)):
        sum1+=x[i][0]
        sum2+=x[i][1]
    return np.array([sum1/len(x), sum2/len(x)])
    
n = 400
d=2
klaster1=klaster2=np.empty([0,2])
a=np.empty([n,2])

#Заполняем общую выборку
h=0
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
#print ("a")
#print (a)
standart1=a[0]
standart2=a[1]
r1=r2=1
#print("standart1")
#print(standart1)
#print("standart2")
#print(standart2)
#print(standart1[0])
#print(standart1[1])
size1=0
size2=1
p=0
distance1=distance2=np.empty([0,1])
k=0
#print(a)
temp_klaster1 = a
#while (size1!=size2):
#while k<1:
while k<10000:
    distance1 = evkl(a, standart1)/r1
    distance2 = evkl(a, standart2)/r2
    for i in range(len(a)):
        if (distance1[i]<distance2[i]):
            klaster1=np.append(klaster1, [a[i]], axis=0)
        else:
            klaster2=np.append(klaster2, [a[i]], axis=0)
    if np.array_equal(temp_klaster1, klaster1):
        break
    standart1 = calcul_standart(klaster1)
    standart2 = calcul_standart(klaster2)
    r1 = calcul_radius(klaster1, standart1)
    r2 = calcul_radius(klaster2, standart2)
    k+=1
    if p==0:
        size1 = len(klaster1) 
        p+=1
    else:
        size2 = len(klaster1)
        p=0
    temp_klaster1 = klaster1
    for i in range(len(klaster1)):
            klaster1=np.delete(klaster1, 0, 0)
    for i in range(len(klaster2)):
            klaster2=np.delete(klaster2, 0, 0)
   
for i in range(len(a)):
        if (distance1[i]<distance2[i]):
            klaster1=np.append(klaster1, [a[i]], axis=0)
        else:
            klaster2=np.append(klaster2, [a[i]], axis=0)

plt.subplot(1,1,1)
for i in range(len(klaster1)):
     plt.plot(klaster1[i][0], klaster1[i][1], "o", color='m')
for i in range(len(klaster2)):
     plt.plot(klaster2[i][0], klaster2[i][1], "o", color='b')
plt.grid(True)
plt.ylabel('X')
plt.xlabel('Y')
plt.title ("Простая форма")
plt.show()

#plt.subplot(1,1,1)
#for i in range(len(a)):
#    if a[i][0]<=50:
#        if a[i][1]<=30:
#            plt.plot(a[i][0], a[i][1], "o", color='g')
#        if a[i][1]> 30:
#            plt.plot(a[i][0], a[i][1], "o", color='b')
#    else:
#        if a[i][1]<=30:
#            plt.plot(a[i][0], a[i][1], "o", color='r')
#        if a[i][1] > 30:
#            plt.plot(a[i][0], a[i][1], "o", color='m')
##plt.ylim(0, min(len(x1), len(x2)))
#plt.grid(True)
#plt.ylabel('X')
#plt.xlabel('Y')
#plt.title ("Простая форма")
#plt.show()  