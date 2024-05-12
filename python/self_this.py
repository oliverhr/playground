


class Node:
	def __init__(self):
		pass

	def _func(self, node):
		if node is self:
			print('soy yo')
		else:
			print('quien es?')


def main():
	node = Node()
	nodo = Node()

	node._func(nodo)
	nodo._func(nodo)

if __name__ == '__main__':
	main()
