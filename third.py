from pprint import pprint
from re import L
from datetime import datetime
import os

def logger(old_function):

    def new_function(*args, **kwargs):
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main_recepies.log', 'a', encoding='utf-8') as file:
            file.write(f'Имя функции - {func_name}, '
                       f'Время вызова функции - {time}, '                       
                       f'аргументы функции - {args, kwargs}, '
                       f'значение функции - {result}, \n'
                       )
        return result

    return new_function

def read_file(f, count):
    i = 0
    
    list_book = []
    while i <= count:
        line = f.readline().strip('\n').split('|')
        #print(line)
        i += 1
        if len(line) == 3:
            book = {}
            book['ingredient_name'] = line[0]
            book['quantity'] = line[1]
            book['measure'] = line[2]
            list_book.append(book)
                    
    return list_book

@logger
def wish_list(dishes, person_count, cook_book):
    list_menu = {}
    for dish in dishes:
        for list in cook_book[dish]:            
            ingredient = {}
            if list['ingredient_name'] in list_menu:
                temp = {}
                temp = list_menu[list['ingredient_name']]
                ingredient['quantity'] = ( int(list['quantity'] ) * person_count) + temp['quantity']
            else:
                ingredient['quantity'] = int(list['quantity']) * person_count
            
            ingredient['measure'] = list['measure']
            list_menu[list['ingredient_name']] = ingredient
    return list_menu



with open('recipes.txt', encoding='utf-8') as f:
    a = True
    cook_book = {}
    while a:
        name = f.readline().strip('\n')
        if name:
            count = int(f.readline())
            cook_book[name] = read_file(f,count)
        else:
            a = False

    print('\nСостав меню:')
    pprint(cook_book)
    
    path = 'main_recepies.log'
    if os.path.exists(path):
        os.remove(path)
        
    menu = wish_list([ 'Омлет', 'Омлет'], 3 , cook_book)
    print('\nКоличество ингредиентов:')
    pprint(menu)