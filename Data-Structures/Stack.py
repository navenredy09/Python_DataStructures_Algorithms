class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop empty stack")

        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item

    def push(self,item):
        self.items.append(item)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to get top of empty stack")

        topIdx = len(self.items)-1
        return self.items[topIdx]

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items=[]

def main():
    s = Stack()
    items = list(range(10))
    items2 = []

    for k in items:
        s.push(k)

    if s.top() == 9:
        print "Test 1 is Passed"
    else:
        print "Test 1 is failed"

    while not s.isEmpty():
        items2.append(s.pop())

    items2.reverse()

    if items2 != items:
        print "Test 2 failed"
    else:
        print "Test 2 is passed"

    try:
        s.pop()
        print "Test 3 is failed"

    except RuntimeError:
        print "Test 3 is passed"

    except:
        print "Test 3 is passed"

    try:
        s.top()
        print "Test 4 is failed"

    except RuntimeError:
        print "Test 4 is passed"

    except:
        print "Test 4 is failed"

if __name__ == "__main__":
    main()
