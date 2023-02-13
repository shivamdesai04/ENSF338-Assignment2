import sys
import json
import timeit
from matplotlib import pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2TestData.json", "r") as file:
    data = json.load(file)

listLengths = []
quicksortTime= []
i = 0

while i < 10:
    listLength = len(data[i])
    elaspedTime = timeit.timeit(lambda : func1(data[i], 0, (listLength - 1) ), number= 1)
    quicksortTime.append(elaspedTime)
    listLengths.append(listLength)

    i += 1

plt.plot(listLengths, quicksortTime)
plt.title("Time taken for Quicksort vs Length of list being sorted")
plt.xlabel("Lenght of List")
plt.ylabel("Execution Time")
plt.show()