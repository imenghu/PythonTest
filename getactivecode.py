import random
import string


def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])


def SaveKey(content):
    with open('Result Key.txt', 'a') as f:
        f.write(content)
        f.write('\n')


if __name__ == '__main__':
    for i in range(20):
        value = GenKey(20)
        print(value)
        SaveKey(value)

chars = string.ascii_letters + string.digits
result = ''.join([random.choice(chars) for i in range(20)])
print(result)
