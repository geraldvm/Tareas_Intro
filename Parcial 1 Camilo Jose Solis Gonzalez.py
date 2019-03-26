"""
    Instituto Tecnológico de Costa Rica (TEC)
    Área Académica de Ingeniería en Computadores

    Camilo José Solís Gonzaléz
    Carné: 2019048742
    
    Curso: Introducción a la Programación
    1 Parcial
    1 Semestre
    
    
"""
#Ejercicio 1

def combinaciones(listaA, listaB):
    if isinstance(listaA, list) and (listaB, list):
        return aux_aux(listaA,listaB,0)
    else:
        return "Error no se ingresaron listas"

def aux_aux(listaA, listaB):
    if listaA ==[] and listaB==[]:
        return []
    elif:
        return(listaA[0], listaB[0])+aux_aux(lista[1:], listaB[B:])
    else:
        return (listaA[1], listaB[1])+aux_aux(lista[1:], listaB[B:])
    
#Ejercicio 2

def std(lista,avg):
    if isinstance (lista,list) and avg>0 and isinstance(avg, int):
        return std_aux(lista,avg)
    else:
        return "Error"

def std_aux(lista,avg):
    if lista == []:
        return[]
    else:
        return math.sqrt(std_aux[(lista[0]+(lista[0]-avg))**2/len(lista)-1])
#Ejercicio 3

def zScore(listaX,S,avg):
    if isinstance[listaX, list] and S>0 and avg>0:
        return calc_list_aux(listaX,avg,S)
    else:
        return "Error"

def calc_list_aux(listaX,S,avg):
    if listX==[]:
        return []
    else:
        return [[listaX[0]-avg]/S]+calc_list_aux(listaX[1:],X,avg)

def rScore(Zx,Zy):
    if residuo >0:
        return 1
    else: return (resultado/n)+calculo_aux(resultado,x)

def calculo2_aux(Zx,Zy):
    if lista ==[]:
        return 0
    else:
        return Zx[0]*Zy[0]+calculo2_aux(Zx[1:],Zy[1:])
