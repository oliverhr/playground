
class Node[T]:
    def __init__(self, data: T)  -> None:
        self.next: Node | None = None
        self.data: T = data


class LinkedList:
    def __init__(self):
        self.first: Node | None = None
        self.last: Node | None = None

    def add[T](self, value: T):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
    def getlast(self):
        return self.last

    def __iter__(self):
        self._current_ = self.first
        return self

    def __next__(self):
        node = self._current_
        if node is None: # if not node
            del self._current_
            raise StopIteration
        self._current_ = node.next
        return node

# -----------------------------------------------------------------------------

def main():
    lista = LinkedList()

    lista.add('primero')
    print('First:', lista.first.data)
    print('Last:', lista.last.data)

    print('-' * 20)
    lista.add('segundo')
    print('First:', lista.first.data)
    print('Last:', lista.last.data)

    print('-' * 20)
    lista.add('tercero')
    print('First:', lista.first.data)
    print('Last:', lista.last.data)

    print('\n', '* ' * 20)
    node = lista.first
    while node:
        print(node.data)
        node = node.next

    print('\n', '# ' * 20)
    for item in lista:
        print(item.data)

if __name__ == '__main__':
    main()
