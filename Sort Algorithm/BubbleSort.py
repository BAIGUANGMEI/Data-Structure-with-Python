def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def BubbleSort_reverse(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    # 冒泡排序的时间复杂度为O(n^2)，空间复杂度为O(1)，是一种稳定的排序算法

    arr = [64, 34, 25, 12, 22, 11, 90]
    # 从小到大排序
    print(BubbleSort(arr))
    # 从大到小排序
    print(BubbleSort_reverse(arr))
    