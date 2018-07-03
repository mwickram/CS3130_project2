def withInsertion(arr):
    import insertionSort as insertion
    return insertion.insertionSort(arr)


def withMerge(arr):
    import mergeSort as merge
    return merge.mergeSort(arr, 0, len(arr) - 1)


def withQuick(arr):
    import quickSort as quick
    return quick.quickSort(arr, 0, len(arr) - 1)