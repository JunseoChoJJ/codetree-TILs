import heapq

N = int(input())

class priorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)  # Max Heap

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -heapq.heappop(self.items)

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if not self.items else 0

    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.items[0]


pq = priorityQueue()

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        num = int(line[1])
        pq.push(num)
    else:
        command = line[0]
        if command == "size":
            print(pq.size())
        elif command == "empty":
            print(pq.empty())
        elif command == "top":
            print(pq.top())
        else:  # pop
            print(pq.pop())
