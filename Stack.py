class Stack:
    def __init__(self):
        self.stack = []

    def Pop(self) -> any:
        if not self.Stack:
            raise IndexError
        return self.stack.pop()

    def Append(self, element: any) -> None:
        self.stack.append(element)

    def Display(self) -> list:
        return (
            self.stack.copy()
        )  # so that if modified outside class it's a copy not the actual stack
