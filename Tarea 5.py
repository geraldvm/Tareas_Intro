class multiplicacion_diagonal(object):
    def __init__(self):
        pass
    
    def matriz(self,matriz1,matriz2):
        if isinstance(matriz1,list) and matriz1!=[] :
            return self.multiplicacion(matriz1,matriz2,0,0,0,0,0)
        
    def multiplicacion(self,matriz1,matriz2,indice,fila,columna,matriz,resultado):
        if indice == len(matriz1):
            return matriz
        elif fila==len(matriz1[0]):
            return self.multiplicacion(matriz1,matriz2,indice+1,0,0,matriz,0)
        elif columna==len(matriz1[0]):
            matriz[indice][fila]= resultado
            return self.multiplicacion(matriz1, matriz2, indice, fila+1, 0, matriz, 0)
        else:
            resultado+= matriz1[indice][columna]*matriz2[columna][fila]
            columna+=1
            return self.multiplicacion(matriz1,matriz2,indice, fila, columna, matriz, resultado)

