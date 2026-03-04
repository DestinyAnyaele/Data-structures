class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class CDL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def Append(self, data: any) -> None:
        if self.head is None:
            self.head = Node(data)
            self.head.next, self.head.prev = self.head, self.head
            self.tail = self.head
        else:
            last_node = self.tail
            last_node.next = Node(data, last_node, self.head)
            self.tail = last_node.next
        self.count += 1

    def Display(self) -> list:
        linkedlist = []
        current_node = self.head
        while current_node is not self.tail:
            linkedlist.append(current_node.data)
            current_node = current_node.next
        if current_node is not None:
            linkedlist.append(current_node.data)
        return linkedlist

    def Length(self) -> int:
        return self.count

    def Insert(self, Index, data):
        if Index < 0:
            Index += self.Length()
        if Index >= self.Length():
            self.Append(data)
        else:
            current_node = self.head
            for i in range(Index - 1):
                current_node = current_node.next
            current_node.next.prev = current_node.next = Node(
                data, current_node, current_node.next
            )
        if Index <= 0:
            self.head.prev = self.head = Node(data, self.tail, self.head)
            self.tail.next = self.head

    def Remove(self, element):
        current_node = self.head
        if current_node is None:
            raise ValueError
        if current_node.data == element:
            self.head = current_node.next
            self.head.prev = self.tail
            return
        while current_node is not self.tail:
            if current_node.data == element:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        if current_node.data == element:
            self.tail = current_node.prev
            current_node.prev.next = self.head
            self.head.prev = current_node.prev
            return
        raise ValueError

    def GetIndex(self, element: any) -> int:
        index = 0
        current_node = self.head
        while current_node is not self.tail:
            if current_node.data == element:
                return index
            current_node = current_node.next
            index += 1
        if current_node.data == element:
            return index
        raise ValueError

    def Pop(self, index=-1) -> Node:
        if index < 0:
            index += self.count
        if index >= self.count:
            raise IndexError("index out of range")
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        if index == 0:
            result = self.head
            if self.count == 1:
                self.head = self.tail = None
            else:
                self.head = current_node.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif current_node.next is self.tail:
            result = self.tail
            current_node.next = self.head
            current_node.next.prev = current_node
            self.tail = current_node
        else:
            current_node.next, result = current_node.next.next, current_node.next
            current_node.next.prev = current_node
        self.count -= 1
        return result.data
