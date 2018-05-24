class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def list_element(self):
        return list(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def list_element(self):
        return list(self.items)


#Implement Stack
stack = Stack()
stack.push(4)
stack.push(6)
print stack.list_element()
print stack.pop()
print stack.top()

#Implement Queue
queue = Queue()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(5)
print queue.list_element()
print queue.dequeue()
print queue.front()

