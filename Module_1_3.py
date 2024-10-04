print('Динамическая типизация')
name = 'Name: Igor'
print(name)
age = 'Age: 35'
print(age)
new_age = 'New age: 36'
print(new_age)
is_student = 'Is Student: True'
print(is_student)

print('Переменные')
number_of_completed_ha = 12
number_of_hours_spent = 1.5
course_name = 'Курс: Python,'
time_fo_one_real = number_of_hours_spent / number_of_completed_ha
print(course_name, 'всего задач:', number_of_completed_ha, ', затрачено часов:', number_of_hours_spent, ', среднее время выполнения ', time_fo_one_real, 'часа.')

print('Строки и индексация строк')
example = 'Пример'
print(example[0])
print(example[-1])
print(example[3:])
print(example[::-1])
print(example[1:6:2])