# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_path(path):
    parts = path.split('/') #разбиваем по слэшу
    file_name_parts = parts[-1].split('.') #последний элемент разбиваем по точке
    file_name, *file_ext_parts = file_name_parts #расширение у нас всё что после первой точки, если точек несколько в имени
    file_ext = '.' + '.'.join(file_ext_parts) if file_ext_parts else '' #собираем обратно расширение файла + исключение если нет расширения
    file_path = '/'.join(parts[:-1]) #собираем путь без последнего элемента
    return file_path, file_name, file_ext


path = 'c:/users/Documents/example.txt'
result = split_path(path)
print(result)