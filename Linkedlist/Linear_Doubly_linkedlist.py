class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LDL:
    def __init__(self):
        self.head = None
        self.count = 0

    def Append(self, element: any) -> None:
        current_node = self.head
        if current_node == None:
            self.head = Node(element)
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(element, current_node)
        self.count += 1

    def Display(self) -> list:
        linkedlist = []
        current_node = self.head
        if current_node != None:
            while current_node.next != None:
                linkedlist.append(current_node.data)
                current_node = current_node.next
            linkedlist.append(current_node.data)
        return linkedlist

    def Length(self) -> int:
        return self.count

    def Remove(self, element: any) -> None:
        current_node = self.head
        if self.Length() == 1:
            if current_node.data is element:
                self.head = None
                self.count = 0
                return
        while current_node.next != None:
            if current_node.data is element:
                if current_node.prev == None:
                    self.head = current_node.next
                    self.head.prev = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                self.count -= 1
                return
            current_node = current_node.next
        if current_node.data is element:
            current_node.prev.next = None
            self.count -= 1
            return
        raise ValueError

    def GetIndex(self, element: any) -> int:
        index = 0
        current_node = self.head
        if self.Length() >= 1:
            while current_node.next != None:
                if current_node.data is element:
                    return index
                index += 1
                current_node = current_node.next
            if current_node.data is element:
                return index
        raise ValueError

    def Pop(self, index=-1) -> Node:
        size = self.Length()
        current_node = self.head
        if index < 0:
            index += size
        if (index >= size) or (index < 0):
            raise IndexError
        else:
            if (index == 0) and (size == 1):
                self.head = None
            elif index == 0:
                self.head = current_node.next
                self.head.prev = None
            else:
                for i in range(index):
                    current_node = current_node.next
                current_node.prev.next = current_node.next
                if current_node.next != None:
                    current_node.next.prev = current_node.prev
        self.count -= 1
        return current_node.data

    def Insert(self, index: int, element: any) -> None:
        size = self.Length()
        current_node = self.head
        if index < 0:
            index += size
        if index >= size:
            self.Append(element)
            return
        elif index < 0:
            self.head = Node(element, None, current_node)
            self.count += 1
            return
        for i in range(index):
            current_node = current_node.next
        current_node.prev.next = Node(element, current_node.prev, current_node)
        self.count += 1
