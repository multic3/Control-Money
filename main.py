from time import sleep, strptime, gmtime
from structure import ControlMoney

name = 'control_money.csv'
cm = ControlMoney(name)
hello_str = 'Hello!'
menu_str = '''\n1. Add\n2. Show all\n3. Show for date\n4. Show by category\n5. Show by cost\n6. Delete\n0. Exit\n
To select the menu function, enter a number (1, 2, 3, 4, 5, 6 or 0) and press Enter:\n'''
flag = True


def check_choice_menu(val):
    while True:
        n = input()
        if n.isdigit() and int(n) in range(0, val + 1):
            return int(n)
        else:
            print(f'InputError: Please enter a number in the range 0 - {val}')


while flag is True:

    print(menu_str)
    print('What would you like to do? ')
    value = check_choice_menu(6)
    if value == 0:
        print('Goodbye!')
        flag = False
    elif value == 1:
        print('Please, fill in the columns: ')
        id_mark = len(cm.file)
        cat, prod, cost = input('Category: '), input('Product: '), float(input('Cost: '))
        while True:
            try:
                date = input('Date in the format YYYY-MM-DD: ')
                if strptime(date, '%Y-%m-%d') <= gmtime():
                    break
                else:
                    print("Invalid date: The date can't be newer than the current!")
            except ValueError:
                print('Invalid format date!')
        cm.file_adder(id_mark, cat.title(), prod.title(), cost, date)
    elif value == 2:
        print(cm.show_by_choice())
    elif value == 3:
        print(cm.show_by_choice('Date'))
    elif value == 4:
        print(cm.show_by_choice('Category'))
    elif value == 5:
        print(cm.show_by_choice('Cost'))
    elif value == 6:
        print('To Delete line enter id')
        id_mark = check_choice_menu(len(cm.file) - 1)
        cm.file_deleter(id_mark)
    sleep(3)
