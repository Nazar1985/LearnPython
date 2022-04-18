import re


s = "4{b3{a}}4{b3{a}}"


def ger_result(s):
    pattern = '\d\{.+\}'
    str_1 = re.findall(pattern, s)
    print(str_1)

if __name__ == '__main__':
    ger_result(s)
# get_result(s) = baaabaaabaaabaaa
