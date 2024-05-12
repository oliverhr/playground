"""
Queues as Doble Linked List
"""

class Node[T]:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Node | None = None
        self.previous: Node | Node = None


class DobleLinkedList:
    def __init__(self, first: Node | None = None,
                 last: Node | None = None) -> None:
        self.first: Node = first
        self.last: Node = last

    def push[T](self, value: T) -> None:
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.previous = self.last
            self.last.next = node
            self.last = node

    def shift(self) -> Node:
        node = self.first
        self.first = self.first.next
        return node


class Queue:
    def __init__(self) -> None:
        self.queue = DobleLinkedList()

    def enqueue[T](self, value: T) -> None:
        self.queue.push(value)

    def dequeue[T](self) -> T:
        node = self.queue.shift()
        return node.data

    def peek[T](self) -> T:
        node = self.queue.first
        return node.data if isinstance(node, Node) else None


# -----------------------------------------------------------------------------
def main() -> None:
    queue = Queue()
    queue.enqueue('primero')
    print('peek:', queue.peek())

    queue.enqueue('segundo')
    print('Dequeue:', queue.dequeue())
    print('peek:', queue.peek())

    queue.enqueue('tercero')
    print('Dequeue:', queue.dequeue())
    print('peek:', queue.peek())

if __name__ == '__main__':
    main()
