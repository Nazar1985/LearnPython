nums = [1, 5, 7, 3]
targets = [12, 13, 55, 66]


def get_result(nums, targets):
    arr = []
    len_nums = len(nums)
    len_targes = len(targets)
    i, j = 0, 1
    while True:
        sum = nums[i] + nums[j]
        if sum in targets:
            index_target = targets.index(sum)
            nums.append(sum)
            arr.append(sum)
            len_nums += 1
            targets.pop(index_target)
            len_targes -= 1
            i = 0
            if len_targes == 0:
                return len(arr)

        j += 1
        if i == len_nums:
            i = 0
            j = i + 1

        if j == len_nums and i != len_nums - 1:

            i += 1
            j = i + 1
        if j == len_nums and i == len_nums - 1:
            return len(arr)

z = get_result(nums, targets)
print(z)
