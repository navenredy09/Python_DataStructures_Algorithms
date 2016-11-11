# Linear Search function in python
# This function will look for an item in a list

def linear_search(myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found

if __name__ == "__main__":
    shopping = ["apple","bananas","chocolate","pasta","orange"]
    item = raw_input("What item do you want to find: ")
    isitFound = linear_search(item,shopping)
    if isitFound:
        print "Your item is in the list"
    else:
        print "Your item is not in the list"
