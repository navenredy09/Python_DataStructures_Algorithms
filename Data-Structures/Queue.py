# Creating Queue class.
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    # q is the object of Queue Class
    q = Queue() 
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)

    print q.dequeue()
