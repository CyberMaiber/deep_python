import random
import string
import os

def generate_random_filename(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def create_random_files():
    extensions = ['.txt', '.mp3', '.jpg', '.bmp', '.doc'] #список расширений файлов
    num_files = random.randint(30, 35) #количество файлов
    
    for _ in range(num_files):
        filename_length = random.randint(6, 8) #количество букв в имени файла
        filename = generate_random_filename(filename_length)
        extension = random.choice(extensions)
        file_path = 'HomeTask7\\'+filename + extension #небольшой костылик

        with open(file_path, 'w') as file:
            file.write('')
        
        print(f"Создан файл: {file_path}")

# Вызываем функцию для создания случайных файлов
create_random_files()