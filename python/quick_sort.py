'''
Quick sort algorithm

terms: pivot, partition, divide and conquer

BigO cases
average = O(n log n)
worst   = O(n^2) depende on the pivot selection
'''


counter: int = 0


def sort(items: list[int]) -> list[int]:
    '''
    Quiecksort se basa en la estrategia "Divide and Conquer"
    particularmente en el concepto llamadao "partitioning"

    Para particionar un array se debe elegir un elemento del
    array de manera aleatoria, a este elemento se le conoce
    como pivote.

    El pivote se usa como base para ordenar los valores menores
    al pivote a la izquierda y los mayores al pivote a la derecha.

    Cada iteración se parte el array en partes con un menor numero
    de elementos (slices). hasta llegar a que el array contenga
    solo un item.
    '''

    # si el tamaño del array es uno no se continua
    if len(items) <= 1: return items

    # por consitencia en esta implementación, se toma
    # como pivote el valor del primer indice.
    # Como el array esta desordenado y teoricamente
    # no se conoce el contenido de cada elemnto
    # se puede considerar que el valor que contiene
    # este elemento del array es aleatorio.
    pivot = items[0]

    # se realiza el ordenamiento del resto de los
    # items a partir del pivote, y se excluye este
    # elemento de de la comparativa
    left = [i for i in items[1:] if i < pivot]
    rigth = [i for i in items[1:] if i >= pivot]

    global counter
    counter += 1
    print(counter, ': ', f'Pivote: {pivot},', 'Slices:', left, rigth)

    # Sobre una recursion de los slices,
    # se regresa el array final ordenado
    return sort(left) + [pivot] + sort(rigth)


def main() -> None:
    items: list[int] = [9, 20, 6, 8, 56, 23, 87, 41, 49, 53]
    print('org: ', items, '\n')
    print('\nsorted:', sort(items))


if __name__ == '__main__':
    main()

