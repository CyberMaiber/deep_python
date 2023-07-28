# Функция получает на вход текст вида: "1-й четверг ноября", "3я среда мая" и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# Научите функцию распозновать не только текстовое название дня недели и месяца, но и числовые, т.е. не мая, а 5.

from datetime import datetime, timedelta
import fnmatch, logging, sys

logging.basicConfig(filename='Hometask15\\converter.log', filemode='a', encoding='utf-8', level=logging.INFO)

def day_of_week_to_num (inp_txt:str):
    '''
    Функция распознания дня недели.

    >>> day_of_week_to_num ('1')
    1
    >>> day_of_week_to_num ('пятн')
    5
    '''
    tmp_dict = {
        'п*н*д*':1,
        'пон*':1,
        'вт*':2,
        'ср*':3,
        'ч*т*':4,
        'п*т*н*':5,
        'пят*':5,
        'с*б*':6,
        'в*с*':7,
    }
    if inp_txt.isdigit():
        if 1<=int(inp_txt)<=7:
            return int(inp_txt)
    else:
        for mask in tmp_dict.items():
            if fnmatch.fnmatch(inp_txt, mask[0]):
                return tmp_dict.get(mask[0])
    return None
    # raise ValueError("Название дня недели не распознано") 

def month_to_num (inp_txt:str):
    '''
    Функция распознания названия месяца
    >>> month_to_num ('1')
    1
    >>> month_to_num ('янвр')
    1
    '''
    tmp_dict = {
        'ян*':1,
        'ф*в*':2,
        'м*р*':3,
        'ап*':4,
        'май*':5,
        'мая*':5,
        'и*н*':6,
        'и*л*':7,
        'ав*':8,
        'с*н*':9,
        'ок*':10,
        'но*':11,
        'н*б*':11,
        'д*к*':12,
        'де*':12
    }
    if inp_txt.isdigit():
        if 1<=int(inp_txt)<=12:
            return int(inp_txt)
    else:
        for mask in tmp_dict.items():
            if fnmatch.fnmatch(inp_txt, mask[0]):
                return tmp_dict.get(mask[0])
    return None
    #raise ValueError("Название месяца не распознано")

def num_to_num(inp_txt:str):
    '''
    Функция распознания номера дня недели в месяце

    >>> num_to_num ('1')
    1
    >>> num_to_num ('пятый')
    5
    '''
    tmp_dict = {
        'пе*':1,
        'вт*':2,
        'тр*':3,
        'че*':4,
        'пя*':5,
    }
    if inp_txt[0].isdigit() and (len(inp_txt) == 1 or not inp_txt[1].isdigit()):
        if 1<=int(inp_txt[0])<=5:
            return int(inp_txt[0])
    else:
        for mask in tmp_dict.items():
            if fnmatch.fnmatch(inp_txt, mask[0]):
                return tmp_dict.get(mask[0])
    return None
    # raise ValueError("Номер дня недели в месяце не распознан, либо некорректен")

def convert_to_nums(text):
    # Распознаём компоненты указанные в строке
    words = text.split()
    month = None
    week_day = None
    day_num = None
    if len(words) == 3:
        month = month_to_num(words[2])
        week_day = day_of_week_to_num(words[1])
        day_num = num_to_num(words[0])
    elif len(words) == 2:
        month = month_to_num(words[1])
        if month == None:
            week_day = day_of_week_to_num(words[1])
            day_num = num_to_num(words[0])
        else:
            week_day = day_of_week_to_num(words[0])
            if week_day == None:
                day_num = num_to_num(words[0])
    elif len(words) == 1:
        month = month_to_num(words[0])
        if month == None:
            week_day = day_of_week_to_num(words[0])
            if week_day == None:
                day_num = num_to_num(words[0])
    else:
        logging.warning("Количество аргументов некорректно. Используются значения по умолчанию.")
    if month == None:
        month = datetime.now().month
        logging.info('Название месяца не распознано. Используется текущий месяц: номер ' + datetime.now().month.__str__())
    if week_day == None:
        week_day = 1
        logging.info('Название дня недели не распознано. Используется номер 1')
    if day_num == None:
        day_num = 1
        logging.info('Номер дня недели в месяце не распознан. Используется номер 1')
    return [day_num,week_day,month]

def convert_nums_to_date(list_of_date:list):
    #считаем перебором количество условных четвергов в месяце и выдаём дату.
    current_year = datetime.now().year
    start_date = datetime(current_year,list_of_date[2],1)
    counter = 0
    while True:
        if list_of_date[1]-1 == start_date.weekday():
            counter += 1
        if counter == list_of_date[0]:
            break
        start_date += timedelta(days=1)
    if list_of_date[2] != start_date.month:
        return None
    else:
        return start_date

#print(convert_nums_to_date(convert_to_nums('5 четв июн')))

if __name__ == "__main__":
    #if len(sys.argv) != 0:
        date = convert_nums_to_date(convert_to_nums(" ".join(sys.argv[1:])))
        if date == None:
            print('Дата не найдена')
        else:
            print('Искомая дата:')
            print(date)
    #else:

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=False)