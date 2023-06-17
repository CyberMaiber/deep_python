# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

text = "Python is an interpreted, high-level, general-purpose programming language.\
    Created by Guido van Rossum and first released in 1991, Python's design philosophy\
     emphasizes code readability with its notable use of significant whitespace. Its \
    language constructs and object-oriented approach aim to help programmers write clear,\
     logical code for small and large-scale projects. Python is dynamically typed and garbage-collected. \
    It supports multiple programming paradigms, including structured (particularly, procedural),\
     object-oriented, and functional programming. Python is often described as a batteries\
     included language due to its comprehensive standard library. An."

# убираем знаки препинания и приводим к нижнему регистру
text = text.lower()
for char in '.,;:?!-':
    text = text.replace(char, '')

# разбиваем текст на слова
words = text.split()

# считаем количество вхождений каждого слова
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# находим 10 самых частых слов
most_common_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]

# выводим результаты
print("Самые частые слова:")
for word, count in most_common_words:
    print(f"{word}: {count}")