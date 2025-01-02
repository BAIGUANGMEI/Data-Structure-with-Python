def SelectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def SelectionSort_reverse(arr):
    for i in range(len(arr)):
        maxIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr

if __name__ == "__main__":
    # 选择排序的时间复杂度为O(n^2)，空间复杂度为O(1)，是一种不稳定的排序算法

    arr = [64, 34, 25, 12, 22, 11, 90]
    # 从小到大排序
    print(SelectionSort(arr))
    # 从大到小排序
    print(SelectionSort_reverse(arr))