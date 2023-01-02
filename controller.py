from model import input_in_data
from model import read_data
from model import find_in_data
from model import import_data
from model import export_data
from model import print_data
from UI import print_UI

def button():
    num = -1
    while num != 0:
        num = print_UI()
        data = read_data()
        match num:
            case 1:
                input_in_data(data)
            case 2:
                find_in_data(data)
            case 3:
                import_data()
            case 4:
                export_data(data)
            case 5:
                print_data(data)
    else:
        print('Конец работы')
