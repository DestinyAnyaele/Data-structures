class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LSL:
    def __init__(self):
        self.head = None

    def Append(self, data: any) -> None:
        current_node = self.head
        if current_node is None:
            self.head = Node(data)
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(data)

    def Display(self) -> list:
        linked_list = []
        current_node = self.head
        if current_node is None:
            return linked_list
        else:
            while current_node.next is not None:
                linked_list.append(current_node.data)
                current_node = current_node.next
            linked_list.append(current_node.data)
            return linked_list

    def Remove(self, element: any) -> None:
        current_node = self.head
        if current_node.data is element:
            self.head = self.head.next
            return
        while current_node.next is not None:
            if current_node.data is element:
                previous_node.next = current_node.next
                return
            previous_node, current_node = current_node, current_node.next
        if current_node.data is element:
            previous_node.next = current_node.next
        else:
            raise ValueError

    def Length(self) -> int:
        count = 0
        current_node = self.head
        if current_node is None:
            return count
        while current_node.next is not None:
            count += 1
            current_node = current_node.next
        count += 1
        return count
        """
        a much better approach is creating a count instance which increases on every Append
        and decreases or every Remove hence time complexity become O(1)
        """

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
            else:
                for i in range(index - 1):
                    current_node = current_node.next
                current_node.next, result = current_node.next.next, current_node.next
            return result.data

    def Insert(self, index: int, element: any) -> None:
        size = self.Length()
        current_node = self.head
        if index < 0:
            index += size
        if index >= size:
            self.Append(element)
            return
        elif index < 0:
            self.head = Node(element)
            self.head.next = current_node
            return
        for i in range(index - 1):
            current_node = current_node.next
        current_node.next, temp = Node(element), current_node.next
        current_node.next.next = temp
