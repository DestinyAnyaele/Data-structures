class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class CSL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def Append(self, element: any) -> None:
        if self.head is None:
            self.head = Node(element)
            self.head.next, self.tail = self.head, self.head
        else:
            self.tail.next = Node(element, self.head)
            self.tail = self.tail.next
        self.count += 1

    def Display(self) -> list:
        current_node = self.head
        last_node = self.tail
        linkedlist = []
        if self.head is None:
            return linkedlist
        while current_node is not last_node:
            linkedlist.append(current_node.data)
            current_node = current_node.next
        linkedlist.append(current_node.data)
        return linkedlist

    def Length(self) -> int:
        return self.count

    def Remove(self, *Elements: tuple):
        for element in Elements:
            current_node = self.head
            while current_node.data != element:
                if current_node is self.tail:
                    raise ValueError
                current_node, previous_node = current_node.next, current_node
            if current_node is self.head:
                if self.Length() == 1:
                    self.head = self.tail = None
                else:
                    self.head = current_node.next
            elif current_node is self.tail:
                self.tail = previous_node
                previous_node.next = self.head
            else:
                previous_node.next = current_node.next
                self.count -= 1

    def Insert(self, Index, Element):
        current_node = self.head
        if Index < 0:
            Index += self.count
        if Index >= self.count:
            self.Append(Element)
            return
        if Index == 0:
            self.head = Node(Element, current_node)
        for times in range(Index - 1):
            current_node = current_node.next
        current_node.next = Node(Element, current_node.next)
        self.count += 1

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
            raise IndexError
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next
        if index == 0:
            result = self.head
            if self.count == 1:
                self.head = self.tail = None
            else:
                self.head = current_node.next
                self.tail.next = self.head
        elif current_node.next is self.tail:
            result = self.tail
            current_node.next = self.head
            self.tail = current_node
        else:
            current_node.next, result = current_node.next.next, current_node.next
        self.count -= 1
        return result.data
