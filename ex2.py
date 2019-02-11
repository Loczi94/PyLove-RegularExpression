import re

def find_dates():
    with open('program_pylove.txt', 'r', encoding='utf8') as program:
        data = program.read()
        found = re.findall(r'201[78]\.\d{2}\.\d{2}', data)
        print(found)
        return found


if __name__ == '__main__':
    find_dates()