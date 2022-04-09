# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:15:46 2020

@author: erika
"""
#ejemplo de peces, cuando C no es actualizado en B
#cuando S esta en B la recompensa final
#es la diferen. de la funcion recom. menos el costo acumu.
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def recompensa(x):
    y=((x/4)-7)**2
    return (50-y)
    
def paro(pi,S,alpha,sumS):
    C=0.5#C es fijo

    fun1=recompensa(len(S))
    fun2=recompensa(len(S)+1)
    Pbarra=np.sum(pi)-sumS#representa la suma de las prob de los que no estan en S
    #si Pbarra es cero ya tenemos todos los tipos de peces
    #print("Pbarra: ")
    #print(Pbarra)
    num=alpha*Pbarra
    beta=fun2-fun1

    if(Pbarra!=0):
        if (beta<=(C/num)):
            return 1#debe de pararse
        else:
            return 0
    else:
        return 1# pues si la suma es cero debe detenerse
    

def buscar(u,alpha,N):#retorna i, el tipo de pez capturado
    for k in np.arange(1,N+1):
        if((u>=((k-1)*alpha)/N)and (u<(k*alpha/N))):
            return k

N=50
X=np.arange(1,N+1,1)
print("ESPACIO DE ESTADOS\n")
print(X)#espacio de estados


C=0
alpha=0.7
#alpha=random.uniform(0,1) #verificar que alpha no sea cero
print("alpha= ")
print(alpha)

pi=np.zeros((1,N+1))#hacemos 31 espacios para dejar el primero vacio
#se tienen tipos del 1 hasta N
#la primera entrada es con k=0

for k in np.arange(1,N+1):#en el ciclo se disminuyen las operaciones 
    pi[0,k] = 1/N

#S vector de tipos de peces distintos
S=[]
rew=[]#servira para graficar, asi tiene
rew.append(recompensa(len(S))-0.5)
#la recompensa cuando la cardinalidad es cero

aux=0
ban=0
sumS=0#esta suma acumulara cada probabilidad del pez que fue capturado
i=N+1 #asi al inicio N no puede estar en peces capturados
elegido=0
safek=0
tope=150
ganancia=0

k=0
while(k<tope):
    C=C+0.5
    u=random.random()

    #simulacion bernoulli
    if(u<=alpha):
        i=buscar(u,alpha,N)

        if(S.count(i)==0):
            S.append(i)
            sumS=sumS+pi[0,i]    
            aux=paro(pi,S,alpha,sumS)    
        
            if(aux==1 and ban==0):
                ban=1
                elegido=len(S)
                print(S)
                sakek=k
                recom=recompensa(len(S))-C
                
            rew.append(recompensa(len(S))-C)
 
    k=k+1

print("elegido= ",elegido)  
print("recom: ",recom)
print("rew18: ",rew[18])
print("rew19: ",rew[19]) 
print("rew20: ",rew[20]) 
ejeX=np.arange(0,len(S)+1,1)

plt.plot(ejeX,rew,'c-o',label='recompensa')
plt.plot(elegido,recom,'r-o',label='elegido')
plt.plot([elegido,elegido],[np.min(rew),recom],'r--')

if(np.max(rew)>recom):
    plt.plot(rew.index(np.max(rew)),np.max(rew),'b-o')
    plt.plot([rew.index(np.max(rew)),rew.index(np.max(rew))],[np.min(rew),np.max(rew)],'b--')
    
plt.ylabel('Recompensa final')
plt.xlabel('Cardinalidad de S')
plt.title("Distintos tipos.")
plt.legend()
plt.show()
