import numpy as np
import random
import matplotlib.pyplot as plt

def sigma(x):
    return 1/(1+np.exp(-x))

def error_f(w2, w3, x, y, b2, b3):
    return 0.5*np.mean(sigma(np.dot(w3, sigma(np.dot(w2, x) +b2)) + b3)-y)**2

x=np.array([[1, 1, 0, 0], [0, 1, 0, 1]])
y=np.array([[1, 0, 0, 1]])
#print(x)
b2 = np.empty([2,1])
b3 = 0
alfa = 10
w2=np.empty([2,2])
w3=np.empty([1,2])
g=0
k=0
e=0.0001
n=4000
test= np.random.uniform(0, 1, (2, n))   
x_Test1 = x_Test2 = np.empty([1,2])
grad_num_mas_w3 = np.empty([1, 2])

for i in range(2):
    for j in range(2):
        w2[i][j] = random.uniform(-0.5,0.5)
for i in range(2):
    w3[0][i]=random.uniform(-0.5,0.5)
    b2[i] = random.uniform(-0.5,0.5)
b3 = random.uniform(-0.5,0.5) 

while k<10000:
    deltaW2=deltaW3=deltab2=deltab3=0
    for i in range(len(x[0])):    
        a = sigma(np.dot(w2, x[:,i]) +b2.T)
        a=a.reshape(2,1)
        out=sigma(np.dot(w3,a)+b3)
        d3=-(y[0][i]-out)*out*(1 - out)     
        d2=np.dot(w3.T,d3)*a*(1 - a)      
        nabla3=np.dot(d3, a.T).T     
        temp = x[:,i]
        nabla2=np.dot(d2, temp.reshape(2,1).T)
        deltaW2 = deltaW2 + nabla2
        deltaW3 = deltaW3 + nabla3
        deltab2 = deltab2 + d2
        deltab3 = deltab3 + d3
        grad_num_mas_w2 = w2
    for j in range(len(w2)):
        for p in range(len(w2[0])):
            w2_temp = w2.copy()
            w2[j][p] = w2[j][p] + e
            grad_num_eps_plus = error_f(w2, w3, x, y, b2, b3)
            w2[j][p]-=2*e               
            grad_num_eps_minus = error_f(w2, w3, x, y, b2, b3)
            w2 = w2_temp
            grad_num_mas_w2[j][p] = (grad_num_eps_plus - grad_num_eps_minus)/(2*e)
    print("численный градиент w2")
    print(abs(grad_num_mas_w2))
    print("ОРШ градиент w2")
    print(abs(deltaW2/len(x[0])))
    print(" ")
    
    for j in range(len(w3[0])):
        w3_temp = w3.copy()
        w3[0][j] = w3[0][j] + e
        grad_num_eps_plus = error_f(w2, w3, x, y, b2, b3)
        w3[0][j]-=2*e               
        grad_num_eps_minus = error_f(w2, w3, x, y, b2, b3)
        w3 = w3_temp
        grad_num_mas_w3[0][j] = (grad_num_eps_plus - grad_num_eps_minus)/(2*e)
    print("численный градиент w3")
    print(abs(grad_num_mas_w3))
    print("ОРШ градиент w3")
    print(abs(deltaW3.T/len(x[0])))
    print(" ")
    
    grad_num_mas_b2 = b2
    for j in range(len(b2)):
        b2_temp = b2.copy()
        b2[j] = b2[j] + e
        grad_num_eps_plus = error_f(w2, w3, x, y, b2, b3)
        b2[j]-=2*e               
        grad_num_eps_minus = error_f(w2, w3, x, y, b2, b3)
        b2 = b2_temp
        grad_num_mas_b2[j] = (grad_num_eps_plus - grad_num_eps_minus)/(2*e)
    print("численный градиент b2")
    print(abs(grad_num_mas_b2))
    print("ОРШ градиент b2")
    print(abs(deltab2/len(x[0])))
    print(" ")
    
    b3_temp = b3
    b3 = b3 + e
    grad_num_eps_plus = error_f(w2, w3, x, y, b2, b3)
    b3-=2*e               
    grad_num_eps_minus = error_f(w2, w3, x, y, b2, b3)
    b3 = b3_temp
    grad_num_mas_b3 = (grad_num_eps_plus - grad_num_eps_minus)/(2*e)
    print("численный градиент b3")
    print(abs(grad_num_mas_b3))
    print("ОРШ градиент b3")
    print(abs(deltab3/len(x[0])))
    print("_____________________________ ")
    
    w2 = w2 - alfa*deltaW2/len(x[0])
    w3 = w3 - alfa*deltaW3.T/len(x[0])
    b2 = b2 - alfa*deltab2/len(x[0])
    b3 = b3 - alfa*deltab3/len(x[0])
#    grad_an =  (deltaW3/len(x[0])).sum() + (deltab3/len(x[0])).sum() 
#    print("ОРШ градиент = ", grad_an)
    a=sigma(np.dot(w2, x) +b2)
    out=sigma(np.dot(w3,a)+b3)
    if out[0][0]>0.9:
        if out[0][1]<0.1:
            if out[0][2]<0.1:
                if out[0][3]>0.9: 
                    k=1000000  
                    break
    k=k+1
    g = g+1
a=sigma(np.dot(w2, x) +b2)
#a=a.reshape(2,1)
out=sigma(np.dot(w3,a)+b3)
print("out = ", np.round(out))
print("g = ", g)

#for i in range(n):
#    a = sigma(np.dot(w2, test) +b2)
##    a=a.reshape(2,1)
#    out=sigma(np.dot(w3,a)+b3)
##print(out)
#
#for i in range(n):
#    if out[0][i]>0.5:
#        x_Test1 = np.vstack((x_Test1, test[:,i]))
#    else:
#        x_Test2 = np.vstack((x_Test2, test[:,i]))
#        
#plt.subplot(1,1,1)
#for i in range(1, len(x_Test1)):
#    plt.plot(x_Test1[i][0], x_Test1[i][1], "o", color='g')
#for i in range(1, len(x_Test2)):
#    plt.plot(x_Test2[i][0], x_Test2[i][1], "o", color='b')
#plt.grid(True)
##plt.ylim(0, 200)
#plt.ylabel('X')
#plt.xlabel('Y')
#plt.title ("Тестовая выборка")
#plt.show() 