# Casos para el nodo a ser eliminado:
# 1.- El nodo es una hoja(leaf), es decir no tiene descendientes
# 2.- El nodo tiene un hijo, es decir tiene un descendiente (izauierdo o derecho)
# 3.- El nodo tiene dos hijos, es decir tiene un descendiente directo de cada lado

def delete(valueToDelete, node):
	# -------------------------
	# Seccion de busqueda
	# -------------------------

	# el final de la recursión no hay mas nodos
	if node is None: return None

	# hacia que lado ir?

	# a la izquirda
	if valueToDelete < node.value:
		node.leftChild = delete(valueToDelete, node.leftChild)
		return

	# a la derecha
	if valueToDelete > node.value:
		node.rightChild = delete(valueToDelete, node.rightChild)
		return

	# -------------------------
	# nos encontramos con el nodo buscado
	# -------------------------
	if valueToDelete == node.value:
		# si tiene un solo descendiente se regresa este
		if node.leftChild is None: return node.rightChild
		if node.rightChild is None: return node.leftChild

		# si se llega a este punto es por que tiene dos hijos
		# se hace un lift para
		node.rightChild = lift(node.rightChild, node)

		# se regresa el nodo a eliminar
		return node


def lift(node, nodeToDelete):
	# si tiene descendientes menores se busca por ese lado
	# hasta llegar al menor de estos
	if node.leftChild:
		node.leftChild = lift(node.leftChild, nodeToDelete)
		return node
	else
		# si se llego al ultimo nodo menor se hace el lift
		# intercambiando los valores del nodo a eliminar
		# con el nodo sucesor
		nodeToDelete.value = node.value
		return node.rightChild

