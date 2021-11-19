import sys
import math


a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
d = b**2 - 4 * a * c

if a == 0:
    if b != 0:
        print(int(-c / b))
elif b == 0 and c != 0:
    if (-c / a) > 0:
        print(int(math.sqrt(-c / a)))
        print(int(-math.sqrt(-c / a)))
elif d == 0:
    print(int(-b / (2 * a)))
elif d > 0:
    print(int((-b + math.sqrt(d)) / (2 * a)))
    print(int((-b - math.sqrt(d)) / (2 * a)))
