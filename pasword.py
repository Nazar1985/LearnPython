def signup():

    name = input("Hello, user, write your nickname: ")
    password = input(f"Hello, {name}, write your password: ")
    repeat = input("repeat your password: ")
    while True:
        if password == repeat:
            print("Welcome back", name)
            break
        else:
            repeat = input("repeat your password .Is wrong.Try again: ")


if __name__ == '__main__':
    signup()
