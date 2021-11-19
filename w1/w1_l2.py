import sys


# print([" " * (int(sys.argv[1]) - x) + ("#" * x) for x in range(1, int(sys.argv[1]) + 1)])
def run():
    n = int(sys.argv[1])
    for i in range(1, n + 1):
        print(" " * (n - i) + ("#" * i))


if __name__ == '__main__':
    run()
