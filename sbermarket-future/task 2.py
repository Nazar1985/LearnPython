array = [4, 'a']


def get_result(array):
    arr = sorted(array)
    if len(arr) >= 3:
        return arr[-1] * arr[-2] * arr[-3]
    elif len(arr) < 3:
        return arr[-1] * arr[-2]
    
    
if __name__ == '__main__':
    print(get_result(array))
