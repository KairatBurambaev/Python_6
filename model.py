import json

def read_data():
    data_list = []
    with open('Data.txt', 'r', encoding = 'utf-8') as datab:
        linelist = datab.readlines()
    
    for line in linelist:
        if line != '':
            data_list.append(line.strip().split(' '))
    return data_list

def rewrite_data(data):
    with open('Data.txt', 'w', encoding = 'utf-8') as datab:

        for line in data:
            datab.write(' '.join(line)+'\n')


def input_in_data(data):

    surname = input('фамилия: ').strip()
    if surname == '':
        surname = '---'
    name = input('Имя: ').strip()
    if name == '':
        name = '---'
    patronymic = input('Отчество: ').strip()
    if patronymic == '':
        patronymic = '---'
    phone = input('Номер телефона: ').strip()
    if phone == '':
        phone = '---'

    line = (surname, name, patronymic, phone)
    data.append(line)

    rewrite_data(data)

def print_line(line):
    print(f'Фамилия: {line[0]}, Имя: {line[1]}, Отчество: {line[2]}, Телефон: {line[3]}')

def find_in_data(data):
    flag = False
    query = input('Введите пользователя: ')
    for line in data:
        for field in line:
            if query == field:
                print_line(line)
                flag = True
    if not flag:
        print('Не найдено')

def print_data(data):
    for line in data:
        print_line(line)

def export_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)

def import_data():
    with open('data.json', 'r') as f:
        return json.load(f)