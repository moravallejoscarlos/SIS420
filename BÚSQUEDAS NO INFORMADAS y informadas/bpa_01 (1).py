# Busqueda en Amplitud - Breadth First Search
from Nodos import Nodo
import random

def busqueda_BPA_solucion(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []

    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # expandir nodos hijo
            estado_nodo = nodo_actual.get_estado()

            # operador izquierdo
            hijo = [estado_nodo[1], estado_nodo[0], estado_nodo[2], estado_nodo[3]]
            hijo_izquierda = Nodo(hijo)
            costo = random.randint(1, 5)
            hijo_izquierda.set_costo(costo)
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)

            # operador central
            hijo = [estado_nodo[0], estado_nodo[2], estado_nodo[1], estado_nodo[3]]
            hijo_centro = Nodo(hijo)
            costo = random.randint(1, 5)
            hijo_centro.set_costo(costo)
            if not hijo_centro.en_lista(nodos_visitados) and not hijo_centro.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_centro)

            # operador derecho
            hijo = [estado_nodo[0], estado_nodo[1], estado_nodo[3], estado_nodo[2]]
            hijo_derecha = Nodo(hijo)
            costo = random.randint(1, 5)
            hijo_derecha.set_costo(costo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_derecha.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)

            hijos = [hijo_izquierda, hijo_centro, hijo_derecha]
            """
            peor_hijo = hijos[0]
            for i, v in enumerate(hijos):
                if v.get_costo() < hijos[i-1].get_costo():
                    peor_hijo = i
            
            hijos = hijos.pop(peor_hijo)
            """
            nodo_actual.set_hijo(hijos)
            


if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
            # 3 + 0 + 0 + 3 = 6
            # 3 + 1 + 1 + 3 = 8
    solucion = [1, 2, 3, 4]
             # 0 + 0 + 0 + 0 = 0
    nodo_solucion = busqueda_BPA_solucion(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
