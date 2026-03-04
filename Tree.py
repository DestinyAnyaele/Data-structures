class Node:
    def __init__(self, value: any, parent=None):
        self.child = []
        self.parent = parent
        self.value = value


class Tree:
    def __init__(self):
        self.tree = []
        self.switch = False

    def Add(self, element: any, parentValue=None) -> None:
        def Recursive(self, va: list) -> bool | None:
            for node in va:
                if self.switch:
                    break
                if node.value == self.parentValue:
                    node.child.append(Node(self.element, node))
                    self.switch = True
                elif node.child:
                    Recursive(self, node.child)

        self.element = element
        self.parentValue = parentValue
        self.switch = False
        if parentValue is None:
            return self.tree.append(Node(element))
        else:
            Recursive(self, self.tree)
        if not self.switch:
            raise ValueError("parent not found")

    def Display(self) -> list:
        # Display is the main function for intial tree;only loops through the initial parents/nodes
        def Recursive(node, temp):
            # This function recursively moves through the tree to find a child(list)
            for i in node.child:
                if i.child:
                    temp[i.value] = {}
                    Recoil(i, temp)
                else:
                    temp[i.value] = None

        def Recoil(test, result):
            # This function moves to the last/latest child in result for addition to dict
            for i, k in result.items():
                if isinstance(k, dict):
                    if i == test.value:
                        Recursive(test, result[i])

        result = {}
        for node in self.tree:
            if node.child:
                result[node.value] = {}
                Recoil(node, result)
            else:
                result[node.value] = None
        return result


obj1 = Tree()
obj1.Add(2)
obj1.Add(1)
obj1.Add(34, 1)
obj1.Add(66, 34)
obj1.Add(666, 66)
obj1.Add("wat", 666)
obj1.Add("war")

import pprint

pprint.pprint(obj1.Display(), indent=2, width=4, depth=True)
print(obj1.Display())
