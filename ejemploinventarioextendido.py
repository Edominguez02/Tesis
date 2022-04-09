# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:42:47 2019

@author: erika
"""


# este codigo fue utilizado en la tesis, 
#es para el ejemplo de inventario extendido
#30/sep/2020
def Suma(XI,x,a,M):
    suma=0
    for s in np.arange(0,len(XI),1):#va de 0 a 5
        suma +=abs(x+a-s)*XI[s]
        
    return suma
    
def Costo(XI,x,a,espxi,M):
    b=5
    h=2
    p=10
    
    C1=b*a
    C2=((h-p)/2)*(x+a-espxi)
    C3=((h+p)/2)*Suma(XI,x,a,M)

    
    return C1+C2+C3

#representa el valor esperado del teorema
#aux es V_t-1, se usa el teorema de valor esperado de una funcion
#se obtiene la prob de que X1=y, entonces por hipotesis
#x1=X0+a-xi, por eso alpha=x+a-y, a repres.a xi
def Sumatoria(aux,XI,X,x,a):
    aux2=copy.deepcopy(aux)
    sumatoria=0
    for y in X:
        alpha=x+a-y
        
        if(0<=alpha<=(len(XI)-1)):
            #print(alpha)
            sumatoria +=aux2[y,0]*XI[alpha,0]
        else:
            sumatoria +=0
    return sumatoria
    
    
    
import numpy as np
import copy
#from random import random
print('\n \t sin umbral\n')
M=5
X=np.arange(0,M+1,1) #espacio de estados
#a=random()#alpha
print('El espacio de estados es:')
print(X)

N=int(input("¿N? "))

#la funcion xi esta definida de 0,...,3
#P(xi=0)=0.4. la probabilidad corresponde con la posicion
#XI=np.array([[0.4],[0.3],[0.2],[0.1]])
#XI=np.array([[0.1],[0.3],[0.2],[0.4]])
XI=np.array([[0],[0.1],[0.1],[0.3],[0.3],[0.2]])
#la funcion arange(4) crea un vector de 0 a 3
#usaremos la esperanza de xi, en este caso es:
espxi=3.4
#tabla de costos
print("tabla de costos")
tab2=np.zeros((M+1,M+1))
for x in X:
    for a in np.arange(0,((M+1)-x),1):#va desde 0 hasta 5-x
        tab2[x,a]=Costo(XI,x,a,espxi,M)
        
        if (x==0 and a==0):#No es necesario
            print(Costo(XI,x,a,espxi,M))
print(tab2)

#recordamos JN(x)=CN(x)=0
#el primer J sera un vector de ceros
J=np.zeros((M+1,1)) #representa C_N
tab2=np.zeros((M+1,M+3))

#calculamos la iteracion N-1,
#la cual solo depende de de C(x,a)
for x in X:
    C=np.zeros(((M+1)-x,1))
    
    for a in np.arange(0,((M+1)-x),1):#va desde o hasta 5-x
        C[a,0]=Costo(XI,x,a,espxi,M)
        tab2[x,a]=C[a,0]
  
    pos_minima=C.argmin()
    J[x,0]=C[pos_minima,0]

    tab2[x,(a+x+1)]=J[x,0]
    tab2[x,(a+x+2)]=pos_minima
print("t= ",N-1)
print(tab2)
aux=np.zeros((M+1,1))

tab2=np.zeros((M+1,M+3))
#calculamos de N-2 a 0
for t in np.arange(N-2,-1,-1):
    
    print("\n t= ",t)
    aux=copy.deepcopy(J)#guardamos el J anterior para usarlo en la sumatoria
    for x in X:
        C=np.zeros(((M+1)-x,1))
        
        for a in np.arange(0,((M+1)-x),1):#va desde o hasta 5-x
            C[a,0]=Costo(XI,x,a,espxi,M)+Sumatoria(aux,XI,X,x,a)
            #redondear a 3 decimales
            tab2[x,a]=round(C[a,0],3)
        #print(C)
        pos_minima=C.argmin()
        #print(pos_minima)
        J[x,0]=C[pos_minima,0]
        tab2[x,(a+x+1)]=round(J[x,0],3)
        tab2[x,(a+x+2)]=pos_minima
    print(tab2)
    #print(aux)
    print(J)


        