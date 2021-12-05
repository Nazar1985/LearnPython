arr = [0, 0, 0, 0]
W = 10

def get_result(arr, w):
    for i in range(0, max(arr)):
        sum_arr = sum(arr)
        if sum_arr <= w:
            return True
        index = arr.index(max(arr))
        a = arr[index] // 2
        arr.pop(index)
        arr.insert(index, a)
        print(i, max(arr), arr, sum_arr, w)
        if i > max(arr):
            return False
    return True


print(get_result(arr, W))
