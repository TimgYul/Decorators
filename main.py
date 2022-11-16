import os
from datetime import datetime


def logger(old_function):

    def new_function(*args, **kwargs):
        time = datetime.now().strftime('%d-%m-%Y - %H:%M:%S')
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'Имя функции - {func_name}, '
                       f'Время вызова функции - {time}, '                       
                       f'аргументы функции - {args, kwargs}, '
                       f'значение функции - {result}, \n')
        return result

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def summator(a, b=0):
        return a + b
        
    @logger
    def div(a, b):
        return a / b

    
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path,encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()