s = "sgdda"
k = 1
stringGoal = "gdd"

def get_result(s, k, string_goal):
    a = s
    w = k
    q = k
    na = 0
    i = 0
    b = True
    while b:
        if a[i] == string_goal[i]:
            na += 1
            i += 1
        else:
            if w > 0:
                a = a[:i] + a[i+1:]
                w -= 1

        if i == len(a) or i == len(string_goal):
            b = False

    b = True
    nz = 0
    j = 0
    z = s[::-1]
    string_goal = string_goal[::-1]
    while b:
        if z[j] == string_goal[j]:
            nz += 1
            j += 1
        else:
            if q > 0:
                z = z[:j] + z[j+1:]
                q -= 1
        if j == len(z) or j == len(string_goal):
            b = False

    return na if na >= nz else nz


x = get_result(s, k, stringGoal)
print(x)
