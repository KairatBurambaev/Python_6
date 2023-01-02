
def print_UI():
    print('-'*50)
    print(' '*11,'***Телефонный справочник***')
    print('-'*50)
    print('1 - Создать новый контакт')
    print('2 - Найти контакт')
    print('3 - Импортировать контакт')
    print('4 - Экспортировать базу справочника')
    print('5 - Распечатать справочник')
    print('0 - закончить работу')

    while True:
        try:
            num = int(input('Выберите необходимое действие: '))
            if num in range(6):
                return num
            else:
                print('Выберите пункты от 0 до 5')
        except ValueError:
            print('Введите число')

