def replaceAndSort(array, deleteItem, insertItem):
    j = 0
    deleteIndex = None
    insertIndex = 0
    for i in array:
        if (j ==0 and array[0]>insertItem):
            insertIndex = 0
            break
        if (j > 0):
            previousItem = array[(j-1)]
            if ((previousItem <= insertItem) and (array[j] > insertItem)):
                insertIndex = j-1
                break
            elif(array[-1] == array[j]):
                insertIndex = j
                break
        j+=1

    j = 0
    for i in array:
        if (deleteItem == i):
            deleteIndex = j
            break 
        j+=1

    if (deleteIndex == None):
        print("The element to be deleted does not exist")
        return None

    if (insertIndex < deleteIndex):
        i = deleteIndex
        insertIndex +=1
        while (i > insertIndex):
            array[i] = array[i-1]
            i-=1
        array[insertIndex] = insertItem

    elif (insertIndex > deleteIndex):
        i = deleteIndex
        while (i < insertIndex):
            array[i] = array[i+1]
            i+=1
        array[insertIndex] = insertItem

    else:
        array[deleteIndex] = insertItem

array = [1,2,5,8,15,20,22]
deleteItem = 5
insertItem = 13
replaceAndSort(array, deleteItem, insertItem)
print(array)