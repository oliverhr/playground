'''
Binary Search Trees
'''
# Al igual que una linked-list los arboles son estructuras basadas
# en nodos, donde cada nodo tiene un link o vinculo hacia multiples
# nodos.
#
#   *     root / raiz / parent            (nivel 1)
#  / \
# *   *   children                        (nivel 2)
#
# Similar a un "arbol genealógico" un nodo tiene como miembros tanto
# ancestros como descendientes, los nodos descendientes son aquellos
# que vienen de una misma raiz.
#
# * En la estructura de "arbol" cada fila de nodo se le conoce como nivel
# * Una propiedad de los arboles es el "balance"
#     - Se dice que un arbol esta balanceado cuando todos los sub-arboles
#       tienen la misma cantidad de nodos de lo contrario se dice que el
#       arbol esta desbalanceado.
#
# Arbol desbalanceado, ya que el sub-arbol izquierdo contiene mas nodos
# que el sub-arbol de la derecha.
#
#      *                                  (nivel 1)
#    /   \
#   *     *                               (nivel 2)
#        /  \
#       *    *                            (nivel 3)
#
# Un "Arbol Binario" es aquel donde cada nodo tiene cero, uno o dos hijos.
#
# Un "Arbol Binario de Busqueda" adicionalmente sigue las siguientes reglas:
#     - Cada nodo tiene como máximo un nodo hijo izquierdo y uno derecho.
#     - Los descendientes izquierdos del nodo solo pueden contener valores
#       que son menores que el valor del nodo.
#     - Los descendientes derechos del nodo solo deben contener valores que
#       son mayores que el valor del nodo.
#
#                50
#              /    \
#            /        \
#          /            \
#        /                \
#       25                75
#     /    \            /    \
#    /      \          /      \
#   10       33       56       89
#  /  \     /  \     /  \     /  \
# 4   11   30  40   52  61   82  95
#                     \
#                     55
#
# Notese que cada nodo tiene descendientes izquiedos con valores menores
# que el de el mismo, y los derechos con valores mayores al valor del nodo.


class Node: pass


class TreeNode(Node):
    def __init__(self,
                 value: int,
                 left: Node | None = None,
                 right: Node | None = None) -> None:
        self.value: int = value
        self.leftChild = left
        self.rightChild = right

    def has_childs(self) -> bool:
        return any([self.leftChild, self.rightChild])


class BinarySearchTree:
    def __init__(self, node: TreeNode | None = None):
        self.root: TreeNode | None = node

    def add(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
            return

        def _recurse(root: TreeNode):
            child = 'leftChild' if value < root.value else 'rightChild'
            if root.__dict__[child] is None:
                root.__dict__[child] = TreeNode(value)
            else:
                _recurse(root.__dict__[child])
        return _recurse(self.root)

    def search(self, target: int) -> TreeNode | None:
        def _recurse(node: TreeNode | None) -> TreeNode | None:
            if not isinstance(node, TreeNode): return None
            if target == node.value: return node
            if target < node.value: return _recurse(node.leftChild)
            if target > node.value: return _recurse(node.rightChild)
        return _recurse(self.root)

    def remove(self, target_value: int) -> None:
        def _root():
            # Sub-case: root has no childs
            if not self.root.has_childs():
                self.root = None
                return

            # Sub-cases: when root has childs
            # right:
            if self.root.leftChild is None:
                self.root = self.root.rightChild
                return
            # left:
            if self.root.rightChild is None:
                self.root = self.root.leftChild
                return

            # two childs:
            leaf = 'rightChild'
            parent = self.root
            if self.root.rightChild.leftChild:
                leaf = 'leftChild'
                parent = _succesor_parent(self.root, 'rightChild')
            return _promote(self.root, leaf, parent)

        def _search(parent: TreeNode, child: str) -> tuple[TreeNode | None, str | None]:
            node = parent.__dict__[child]
            if not isinstance(node, TreeNode): return None, None
            if target_value == node.value: return parent, child
            if target_value < node.value: return _search(node, 'leftChild')
            if target_value > node.value: return _search(node, 'rightChild')

        def _delete(parent: TreeNode, child: str | None) -> None:
            node = parent.__dict__[child]
            # Case: zero childs
            if not node.has_childs():
                parent.__dict__[child] = None
                return

            if node.has_childs():
                # Case: single child either right or left
                if node.leftChild is None: return _lift(parent, 'rightChild', 'leftChild')
                if node.rightChild is None: return _lift(parent, 'leftChild', 'rightChild')

                # Case: two childs
                succesor = {
                    'leaf': 'rightChild',
                    'parent': node,
                }
                if node.rightChild.leftChild:
                    succesor['leaf'] = 'leftChild'
                    succesor['parent'] = _succesor_parent(node, 'rightChild')

                return _promote(node, **succesor)

        def _succesor_parent(parent: TreeNode, child: str = 'leftChild') -> TreeNode:
            node = parent.__dict__[child]
            if node.leftChild is not None:
                return _succesor_parent(node)
            return parent

        def _lift(parent: TreeNode, child: str, node: str) -> None:
            origin = parent.__dict__[node]
            target = origin.__dict__[child]
            parent.__dict__[node] = target

        def _promote(target: TreeNode, leaf: str, parent: TreeNode) -> None:
            '''
            Change the target value with the succesor value,
            then remove the reference for the succesor node
            from its parent.

            If succesor has a left child, the referece is attached to the
            parent of the succesor leaf.
            '''
            node = parent.__dict__[leaf]

            target.value = node.value
            parent.__dict__[leaf] = None

            if node.rightChild is not None:
                _lift(parent, 'leftChild', 'rightChild')

        # ---------------------------------------------------------------------
        # Remove runner
        # Case: root is the target
        if self.root.value == target_value:
            return _root()
        # if not root search for item, get parent node and parent leaf
        ancestor, descendant = _search(self.root,
                                       'leftChild' if target_value < self.root.value else 'rightChild')
        return _delete(ancestor, descendant) if ancestor and descendant else None


# -----------------------------------------------------------------------------
def factory():
    bst = BinarySearchTree()
    items = [50, 25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95]
    for item in items:
        bst.add(item)
    return bst


def traverse(bst):
    from enum import Enum

    class Order(Enum):
        PREORDER = -1
        INORDER = 0
        POSTORDER = 1

    def _print_tree(node: TreeNode, order: Enum = Order.INORDER) -> None:
        # if there is nothing more stop
        if node is None: return

        # Way of traversing - Pre
        if order == Order.PREORDER: print(node.value, end=' ')

        # ---------------------------------------------------------------------
        _print_tree(node.leftChild, order)
        # ---------------------------------------------------------------------

        # Way of traversing - In (default)
        if order == Order.INORDER: print(node.value, end=' ')

        # ---------------------------------------------------------------------
        _print_tree(node.rightChild, order)
        # ---------------------------------------------------------------------

        # Way of traversing - Post
        if order == Order.POSTORDER: print(node.value, end=' ')

    # traverse over the bst
    print('\nPre Order:', end=' ')
    _print_tree(bst.root, Order.PREORDER)

    print('\nIn Order:', end=' ')
    _print_tree(bst.root, Order.INORDER)

    print('\nPost Order:', end=' ')
    _print_tree(bst.root, Order.POSTORDER)


def max_value(bst):
    # function to get the max value on the tree
    def max(node):
        return max(node.rightChild) if node.rightChild else node.value
    print('\nMax', max(bst.root))


def values_breath_depth_iteration(bst):
    """
    La clave y diferencia esta en la estructura de datos utilizada
    para realizar el recorrido del arbol.

    - Stack para profundidad:
        agrega primero la rama derecha y luego la izquierda
    - Queue para amplitud:
        agrega primero la rama derecha y luego la derecha

    Se puede utilizar Collections.deque que funciona como Cola y como Pila,
    no se hace diferencia en como se agregan los elementos a la coleccion,
    la diferencia principal es de donde se toma el elemento a remover:
        - Stack[LiFo]: últimos en ingresar
        - Queue[FiFo]: primeros en ingresar
    """

    # IIFE: Inmediatelly Invoked Function Expression
    # "@lambda _: _()" <- this decorator converts this function in a IIFE

    # profundidad primero
    @lambda _: _()
    def depth_first():
        from collections import deque as Stack

        def values(root):
            values = []
            if root is None: return values

            stack = Stack([root])
            while len(stack):
                current = stack.pop()   # toma el elemento final de la lista
                values.append(current.value)

                if current.rightChild: stack.append(current.rightChild)
                if current.leftChild: stack.append(current.leftChild)
            return values
        print('Depth First Traverse:', values(bst.root))

    # amplitud primero
    @lambda _: _()
    def breadth_first():
        from collections import deque as Queue

        def values(root):
            values = []
            if root is None: return values

            queue = Queue([root])
            while len(queue):
                current = queue.popleft()   # toma el elemento inicial de la lista
                values.append(current.value)

                if current.leftChild: queue.append(current.leftChild)
                if current.rightChild: queue.append(current.rightChild)
            return values
        print('Breadth First Traverse:', values(bst.root))


def main():
    bst = factory()

    traverse(bst)

    bst.add(55)
    max_value(bst)
    values_breath_depth_iteration(bst)


# def test():
#     bst = factory()
#     bst.add(55)

#     node = bst.search(11)
#     print('value', node.value)
#     print('has_childs', node.has_childs())
#     print('leftChild', node.leftChild, node.leftChild.value if node.leftChild else '- - - -')
#     print('rightChild', node.rightChild, node.rightChild.value if node.rightChild else '- - - -')

#     node = bst.search(52)
#     print('value', node.value)
#     print('has_childs', node.has_childs())
#     print('leftChild', node.leftChild, node.leftChild.value if node.leftChild else '- - - -')
#     print('rightChild', node.rightChild, node.rightChild.value if node.rightChild else '- - - -')

#     bst.remove(10)
#     node = bst.search(25)
#     print('value', node.value)
#     print('has_childs', node.has_childs())
#     print('leftChild', node.leftChild, node.leftChild.value)
#     print('rightChild', node.rightChild, node.rightChild.value)


#     bst.remove(75)
#     node = bst.search(82)
#     print(node if node else '- / '*20)
#     if isinstance(node, TreeNode):
#         print('value', node.value)
#         print('has_childs', node.has_childs())
#         print('leftChild', node.leftChild, node.leftChild.value if node.leftChild else '- - - -')
#         print('rightChild', node.rightChild, node.rightChild.value if node.rightChild else '- - - -')

#     bst.remove(75)
#     print('ok - ' * 20)
#     bst.remove(75)

#     bst.remove(52)
#     node = bst.search(56)
#     print(node if node else '- / '*20)
#     if isinstance(node, TreeNode):
#         print('value', node.value)
#         print('has_childs', node.has_childs())
#         print('leftChild', node.leftChild, node.leftChild.value if node.leftChild else '- - - -')
#         print('rightChild', node.rightChild, node.rightChild.value if node.rightChild else '- - - -')

#     bst.remove(50)
#     node = bst.search(52)
#     print('root', bst.root.value)
#     print(node if node else '- / '*20)
#     if isinstance(node, TreeNode):
#         print('value', node.value)
#         print('has_childs', node.has_childs())
#         print('leftChild', node.leftChild, node.leftChild.value if node.leftChild else '- - - -')
#         print('rightChild', node.rightChild, node.rightChild.value if node.rightChild else '- - - -')


# def demo():
#     node = TreeNode(25)
#     root = TreeNode(50, node, right=TreeNode(75))
#     bst = BinarySearchTree(root)

#     result = bst.search(75)
#     print(result, result.value)

#     bst.add(10)
#     bst.add(4)

#     result = bst.search(4)
#     print(result, result.value)

#     bst.add(33)
#     bst.add(30)
#     bst.add(40)

#     result = bst.search(33)
#     print(result, result.value)
#     print(result.leftChild.value, result.rightChild.value)


if __name__ == '__main__':
    main()
