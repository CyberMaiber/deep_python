

import csv


class NameValidator:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        temp = value.split(" ")
        for val in temp:
            if not val.isalpha():
                raise ValueError("ФИО должно состоять только из букв")
            if not val[0].isupper():
                raise ValueError("ФИО должно начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Student:
    
    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self._subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                subject = row[0]
                #print(row)
                self._subjects[subject] = {'grades': [], 'test_results': []}
    

    def add_grade(self, subject, grade):
        if subject in self._subjects:
            if grade >= 2 and grade <= 5:
                self._subjects[subject]['grades'].append(grade)
            else:
                raise ValueError("Оценка должна быть от 2 до 5")
        else:
            raise ValueError("Предмет не существует")

    def add_test_result(self, subject, result):
        if subject in self._subjects:
            if result >= 0 and result <= 100:
                self._subjects[subject]['test_results'].append(result)
            else:
                raise ValueError("Результат теста должен быть от 0 до 100")
        else:
            raise ValueError("Предмет не существует")

    
    def get_subject_avg_grade(self, subject):
        if subject in self._subjects:
            grades = self._subjects[subject]['grades']
            if grades:
                return sum(grades) / len(grades)
            else:
                return 0
        else:
            raise ValueError("Предмет не существует")

    
    def get_overall_avg_grade(self):
        all_grades = [grade for subject in self._subjects.values() for grade in subject['grades']]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0

    def get_subject_avg_tests(self, subject):
        if subject in self._subjects:
            tests = self._subjects[subject]['test_results']
            if tests:
                return sum(tests) / len(tests)
            else:
                return 0
        else:
            raise ValueError("Предмет не существует")

    
    def get_overall_avg_tests(self):
        all_tests = [tests for subject in self._subjects.values() for tests in subject['test_results']]
        if all_tests:
            return sum(all_tests) / len(all_tests)
        else:
            return 0

# Пример использования класса

student = Student("Иванов Иван Иванович", "HomeTask12\pred.csv")
print(student.name)
student.add_grade("Математика", 4)
student.add_grade("Математика", 5)
student.add_grade("Физика", 3)
student.add_grade("Физика", 4)
student.add_grade("История", 5)

student.add_test_result("Математика", 85)
student.add_test_result("Математика", 92)
student.add_test_result("Физика", 78)
student.add_test_result("Физика", 87)
student.add_test_result("История", 95)

print(student.get_subject_avg_grade("Математика"))
print(student.get_subject_avg_grade("Физика"))
print(student.get_subject_avg_grade("История"))

print(student.get_subject_avg_tests("Математика"))
print(student.get_subject_avg_tests("Физика"))
print(student.get_subject_avg_tests("История"))

print(student.get_overall_avg_grade())
print(student.get_overall_avg_tests())

