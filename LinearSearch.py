import random

def LinearSearch(itemList,elementToSearch,listSize): #Function parameters : i)list of items, ii) element to be searched and iii) size of the list 
    for index in range(0,listSize):
        if itemList[index] == elementToSearch:
            return index
    return "Number not found"

def generateRandomList():
    itemList = []
    listSize = int(input()) #Enter the size of the list
    lowerBond = int(input()) #Enter the lower bond of the possible integers
    upperBond = int(input()) #Enter the upper bond of the possible integers
    for index in range(0,listSize):
        itemList.append(random.randint(lowerBond,upperBond)) #Appending the random integers into the list
    elementToSearch = int(input()) #Enter the integer to be searched for
    index = LinearSearch(itemList,elementToSearch,listSize) #Function returning index of the elementToSearch
    return index

def main():
    index = generateRandomList()
    print(index)
    
if __name__ == "__main__":
    main()
