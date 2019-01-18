from string import ascii_letters, digits
from random import choices
from sys import argv


def randstr(length):
    return ''.join(choices(ascii_letters + digits, k=int(length)))


if __name__ == '__main__':
    str_length = argv[1]
    print(randstr(str_length))
