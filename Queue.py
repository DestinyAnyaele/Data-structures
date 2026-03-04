class Queue:
    def __init__(self):
        self.queue = []

    def Append(self, element) -> None:
        self.queue.append(element)

    def Pop(self) -> any:
        if not self.queue:
            raise IndexError
        return self.queue.pop(0)

    def display(self) -> list:
        return self.queue.copy()
