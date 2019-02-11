import re


def count_python():
    with open('wikipedia_python.txt', 'r', encoding='utf8') as wiki:
        data = wiki.read()
        found = re.findall(r'[Pp]ython', data)
        print(len(found))

if __name__ == '__main__':
    count_python()