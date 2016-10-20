# Binary Search function in Python
# This function will look for an item in a list by dividing
# the list in half every time it searches

def binary_search(myItem,myList):
    found = False
    bottom = 0
    top = len(myList) -1 
    top=len(myList)-1
    while bottom <= top and not found:
        middle = (bottom + top) //2
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle -1
    return found

if __name__ == "__main__":
    numberList = [1,4,6,8,12,15,18,19,21,27]
    item = int(raw_input("What are number you aree looking for? "))
    isitFound = binary_search(item,numberList)
    if isitFound:
        print "Your number is in the list!"
    else:
        print "Your number is not present in the list"
        
