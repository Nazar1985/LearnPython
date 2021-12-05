# def get_result1(array_start, array_goal):
#     f = len([True for i in range(len(array_start)) if not array_start[i] == array_goal[i]]) // 2
#     return f


def get_result(array_start, array_goal):
    len_goal = len(array_goal)
    i, j, n = 0, 0, 0
    while True:
        print(array_goal)
        print(array_start)
        print(n, i, j)
        if array_goal[j] == array_start[j]:
            j += 1
        elif array_goal[j] == array_start[i] and array_goal[j] != array_start[j]:
            array_start[i], array_start[j] = array_start[j], array_start[i]
            print("if", array_goal)
            print("if", array_start)
            n += 1
            j += 1
            i = 0
        if i == len_goal - 1:
            print('end i')
            i = 0
            j += 0
        if array_goal == array_start:
            print("return", array_goal)
            print("return", array_start)
            return n
        elif n == 20:
            return n
        i += 1

array_goal = [5, 3, 4, 2]
array_start = [4, 5, 2, 3]
z = get_result(array_start, array_goal)
print(z)