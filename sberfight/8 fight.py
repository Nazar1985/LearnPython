# Не стал доделывать

# scheme = ['0-0-0-0', '1-1-1-0', '0-0-1-0', '0-0-1-0']
# scheme = ["0-0-0-0", "1-1-1-0", "0-0-1-0", "0-0-1-0"]
scheme = ["0, 0, 1, 0, 0, 0, 0, 0",
          "0, 0, 1, 0, 1, 1, 1, 0",
          "0, 0, 1, 1, 1, 0, 1, 0",
          "0, 0, 0, 0, 0, 0, 1, 0",
          "0, 0, 0, 0, 0, 0, 1, 0",
          "0, 0, 0, 0, 1, 1, 1, 0",
          "0, 0, 0, 0, 1, 0, 0, 0"
          ]  # 268
# scheme = ['0-0-0-0', '1-1-1-0', '0-0-1-0', '0-0-1-0']
# scheme = ['0-0-0-0', '1-1-1-0', '0-0-1-0', '0-0-1-0']


def get_result(scheme):
    grand_sum = 0
    ugol_1, ugol_2, ugol_3, ugol_4 = 10, 13, 15, 17
    vert, gor = 20, 21
    tr_up, tr_left, tr_down, tr_right = 29, 31, 32, 40
    krest = 63
    arr = []
    for y in scheme:
        row = []
        if '-' in y:
            for x in y.split('-'):
                row.append(x.strip())
        elif ',' in y:
            for x in y.split(','):
                row.append(x.strip())
        elif '.' in y:
            for x in y.split('.'):
                row.append(x.strip())
        arr.append(row)
    y = len(arr)
    x = len(arr[0])

    if arr[0][0] == '0' and arr[0][1] == '1' and arr[0][2] == '0':
        grand_sum += 20
    elif




f = get_result(scheme)
print(f)
