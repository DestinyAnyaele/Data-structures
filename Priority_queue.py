class PriorityQueue:
    def __init__(self):
        self.Queue = []

    def Add(self, element: any, priority: int) -> None:
        """
        I used an int type to classify priority why ?
        it's much easier to implement and it's has infinity cases
        since numbers are inexhaustible (infinity)
        one could have a billion or million priorities
        """
        import operator

        self.Queue.append((element, priority))
        self.Queue.sort(key=operator.itemgetter(1))

    def Display(self) -> list:
        return self.Queue

    def Pop(self) -> any:
        if not self.Queue:
            raise IndexError
        return self.Queue.pop(0)[0]

    def ChangePriority(self, element: any, new_priority: int) -> None:
        for I in self.Queue:
            if I[0] == element:
                self.Queue.remove(
                    I
                )  # using pop is better O(1) but I'm lazy remove uses O(n)
                self.Add(element, new_priority)
                break
        else:
            raise ValueError

    """
  I didn't use any in-built method - heapq
  my method above works for priority queue 
  but due to the sorting on every Add the
  time complexity becomes O(n²Log(n),no way to improve unless 
  with the heapq module which sorts internally 
  Even if I tried sorting before pop function,the time
  complexity still remains O(n²log(n))
  """


class PQueue:  # a more optimized version
    from heapq import heappop, heappush, heapify

    def __init__(self):
        self.queue = []

    def Append(self, element: any, priority: int) -> None:
        heappush(self.queue, (priority, element))

    def Pop(self):
        if not self.queue:
            raise IndexError
        return heappop(self.queue)[1]

    def Display(self) -> list:
        return self.queue.copy()

    def ChangePriority(self, element: any, new_priority: int) -> None:
        for I in self.queue:
            if I[1] == element:
                self.queue.remove(I)
                heapify(self.queue)
                heappush(self.queue, (new_priority, element))
                break
        else:
            raise ValueError
