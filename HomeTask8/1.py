# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def detour_directory(directory):
    result = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        # Получаем путь относительно исходной директории
        rel_path = os.path.relpath(root, directory)
        is_dir = True

        # Для каждой директории сохраняем её размер с учётом всех вложенных файлов и директорий
        if rel_path != '.':
            dir_size = sum(os.path.getsize(os.path.join(root, file))
                           for file in files)
            total_size += dir_size
            result.append(
                {'path': rel_path, 'type': 'directory', 'size': dir_size})

        # Для каждого файла сохраняем его размер
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
            result.append({'path': os.path.join(rel_path, file),
                          'type': 'file', 'size': file_size})

    # Добавляем информацию о директории и общем размере
    result.append({'path': '.', 'type': 'directory', 'size': total_size})

    return result


def save_to_csv(results, output_file):
    field_names = ['path', 'type', 'size']

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerows(results)


def save_to_json(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)


def save_to_pickle(results, output_file):
    with open(output_file, 'wb') as file:
        pickle.dump(results, file)


directory = r'C:\Users\Voice\Desktop\LessonsPython'  # Укажите путь к директории

results = detour_directory(directory)

os.chdir('HomeTask8')  # смена рабочего каталога
save_to_csv(results, 'results.csv')
save_to_json(results, 'results.json')
save_to_pickle(results, 'results.pickle')
