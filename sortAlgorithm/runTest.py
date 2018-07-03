import random
import sys
sys.setrecursionlimit(100000)
import time
import sort
#Author: Praminda Mahesh Imaduwa-Gamage, UMSL
#CMP3130: Algorithm Analysis and Design, Programming Assignment - 2 11/05/2017

def getMeanExecutionTime(sortAlgo, arraySize):

    size = arraySize
    ListRange = size * 100
    num_runs = 500
    timeList = list()

    for i in range(0, num_runs):

        random.seed(100)
        arr = random.sample(range(ListRange), size)
        start_time = time.time()

        if sortAlgo == 'QuickSort':
            sort.withQuick(arr)
        if sortAlgo == 'MergeSort':
            sort.withMerge(arr)
        if sortAlgo == 'InsertionSort':
            sort.withInsertion(arr)
        timeList.append(1000 * (time.time() - start_time))

    return sum(timeList) / len(timeList)


print("------ Average time from 500 runs -------", "\n")
sortAlgorithm = ['InsertionSort', 'MergeSort', 'QuickSort']

for sortType in sortAlgorithm:
    print("Sort Algorithm: ", sortType, '\n')
    for size in [100, 200, 500, 800, 1500]:
        print(size, " size array sorted in ", "%0.3f ms " % getMeanExecutionTime(sortType, arraySize = size))
    print("--------")

