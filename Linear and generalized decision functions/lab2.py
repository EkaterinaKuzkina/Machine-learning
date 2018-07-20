import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import numpy as np
import random
import math
import pylab
from numpy.linalg import inv
n = 1000
nX=25
a=np.empty([n,2])
test=x1Test=x2Test=np.empty([0,2])
#Заполняем общую выборку
for i in range(n):
    for j in range(2):
        if j % 2 == 0:
            a[i][j] = random.randint(0,100)
        else:
            a[i][j] = random.randint(40,150)
k=math.ceil(n*6/10)
x_teacher=test=np.empty([0,3])
t=np.empty([0,1])
#Простая форма
for i in range(k):
    for j in range(2):
         if j % 2 == 0:
            if a[i][j] < 40:
                x_teacher=np.append(x_teacher, [[1,a[i][j],a[i][j+1]]], axis=0)
                t=np.append(t, [[1]], axis=0)
            if a[i][j] > 55:
                x_teacher=np.append(x_teacher, [[1,a[i][j],a[i][j+1]]], axis=0)
                t=np.append(t, [[-1]], axis=0)
w=np.dot(np.dot(inv(np.dot(x_teacher.T, x_teacher)), x_teacher.T), t)
for i in range(n-k):
    test=np.append(test, [[1,a[k][0],a[k][1]]], axis=0)
    k=k+1
for i in range(len(test)):
    s=0
    for j in range(len(w)):
        s=s+test[i][j]*w[j] 
    if s>0:
        x1Test=np.append(x1Test, [[test[i][1],test[i][2]]], axis=0)
    else:
        x2Test=np.append(x2Test, [[test[i][1],test[i][2]]], axis=0)
#        
plt.subplot(1,1,1)
for i in range(len(x_teacher)):
    if t[i]>0:
        plt.plot(x_teacher[i][1], x_teacher[i][2], "o", color='g')
    else:
        plt.plot(x_teacher[i][1], x_teacher[i][2], "o", color='b')
#plt.ylim(0, min(len(x1), len(x2)))
plt.grid(True)
plt.ylim(0, 200)
plt.ylabel('X')
plt.xlabel('Y')
plt.title ("Простая форма")
#
plt.show()
plt.subplot(1,1,1)
for i in range(len(x1Test)):
    plt.plot(x1Test[i][0], x1Test[i][1], "o", color='b')
for i in range(len(x2Test)):
    plt.plot(x2Test[i][0], x2Test[i][1], "o", color='g')
#plt.ylim(0, min(len(x1), len(x2)))
plt.grid(True)
plt.ylim(0, 200)
plt.ylabel('количество ошибок')
plt.xlabel('количество элементов в обучающей выборке')
plt.title ("Зависимость количества ошибок от размера обучающей выборки")
plt.show()