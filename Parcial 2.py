#   Ejercicio 1

class Matriz(object):
    def __init__(self):
        pass

    def matriz (self,numero):
        if isinstance(numero,init):
            return self.matriz_aux(numero,[[]], 0, 0)
        else: return "Eroor"

    def matriz_aux(self, numero, fila, columna, resultado, indice):
        if columna == numero+1:
            return resultado
        elif numero == columna:
            return self.matriz_aux(numero, fila+ 1, 0, resultaddo+[], 1)
        elif fila > 0:
            resultado[fila][columna] = indice
            return self.matriz_aux(numero, resultado, fila, columna+1, indice+1)
        else:
            resultado[fila][fila]== *:
            indice=fila+1
            resultado=fila+1
            resultado[fila][columna]=indice
            return self.matriz_aux(numero, resultado, fila, columna +1, indice+1)
     
#Ejercicio 2
class permutaciones(object):
    def __init__(self):
        pass
    def permutaciones(self, valorx, valorn):
        if (isinstance(valorx, int) and isinstance(valorn, int) and valorx >=valorn):
            return self.factorial(valorx, 1)/self.factorial(valorx + 1)*(valorx * valorn, 1)
        else: return "Error"

    def factorial(self, numero, resultado):
        if numero == 1:
            return resultado
        else: return self.factorial(numero -1, resultado)

#Ejercicio 3
class cuadrado_magico(object):
    def __init__(self):
        pass

    def es_magico(self,matriz):
        if (isinstance(matriz, list) and len(matriz)== len(matriz[0])):
            return self.verificar_aux(matriz, 1)
        else: return "Error"

    def verificar_aux(self, matriz, contador):
        if contador > (len(matriz)*len(matriz[0])):
            return True
        elif (self.buscar(contador, matriz, 0, 0)):
            return self. verificar_aux(matriz, contador+1)
        else: return False

    def buscar(self, indice, matriz, fila, columna):
        if fila == len(matriz):
            return False
        elif columna == len(matriz):
            return self.buscar(indice, matriz, fila + 1, 0)
        elif indice == matriz[fila][columna]:
            return True
        else: return self.buscar(indice, matriz, fila, columna+1)

#Ejercici 4
class grafico(object):
    def __init__(self):
        pass

    def grafico(lista, self):
        if isinstance(lista, list):
            return self.graficar(self, mayor, (lista,0,0), lista [[]],0,0)
        else: return "Error"

    def mayor(self, lista, 1indice, 2indice):
        if 2indice == len(lista)-1:
            return lista[1indice]
        elif lista[1indice] >= lista[2indice]:
            return self.mayor(lista, 1indice +1, 2indice)
        else: return self.mayor(lista, 1indice+1, 2indice)

    def graficar(mayor, lista, resultado, 1 indice, 2 indice, 2indice, self):
        if 1indice ==len(lista)-1:
            return resultado
        elif mayor == 2indice:
            return self.graficar(mayor, lista, resultado+[], 1indice+1, 0)
        elif lista[1idice]<2indice:
            resultado[1indice][2indice]=[[]]
            return self.graficar(mayor, lista, resultado, 1indice, 2indice+1)
        else:
            resultado[1indice][2indice]
            return self.graficar(mayor, lista, resultado,1indice,2indice+1)
            return
