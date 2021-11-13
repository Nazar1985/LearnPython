import sys


# print(sum([int(x) for x in sys.argv[1]]))
def run():
    digit_string = sys.argv[1]
    s = 0
    for i in digit_string:
        s += int(i)
    return s


if __name__ == '__main__':
    print(run())
