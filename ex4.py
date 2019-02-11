import re


def switch_letters():
    with open('celebrities.txt', 'r', encoding='utf8') as celebrities:
        for line in celebrities.readlines():
            line_changed = re.sub(r'(\w)(\w+) (\w)(\w+)',r'\3\2 \1\4' , line)
            print(line_changed)

if __name__ == '__main__':
    switch_letters()