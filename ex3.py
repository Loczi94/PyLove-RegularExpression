import re

def workshop_info():
    counter = 0
    dict_program = {}
    with open('program_pylove.txt', 'r', encoding='utf8') as program:
        for line in program.readlines():
            found = re.search(r'\d{4}\.\d\d\.\d\d', line)
            if found:
                counter += 1
                words = re.split(r' - ',line)
                dict_lesson = {}
                dict_lesson['date'] = words[0]
                dict_lesson['title'] = words[1]
                if len(words)>2:
                    dict_lesson['leading_mentor'] = words[2]
                else:
                    dict_lesson['leading_mentor'] = ''
                dict_program[counter] = dict_lesson
        print(dict_program)


if __name__ == '__main__':
   workshop_info()

# Regular expression:
# (\d{4}\.\d{2}\.\d{2}) - (.+)

# workshop_list = re.findal(r'(\d{4}\.\d{2}\.\d{2}) - (.+)', data)
# workshops = {}
# for workshop_number, (data, info) in enumerate(workshop_list):
#   info = re.split(r' - ', info)
#   workshop[workshop_number] = {
#       'date' : data,
#       'title':
#       'mentor': '' if len(info) == 1 else info[-1]
#   }