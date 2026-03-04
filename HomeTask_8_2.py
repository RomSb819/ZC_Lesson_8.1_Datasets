# Задание: Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# Самостоятельно создайте DataFrame с данными
# Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# Вычислите среднюю оценку по каждому предмету
# Вычислите медианную оценку по каждому предмету
# Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# можно также попробовать рассчитать IQR
# Вычислите стандартное отклонение

import pandas as pd
import random

names = ('Анна','Ваня','Толя','Катя','Маша','Федя','Полина','Ника','Вася','Боря')


def grade_random(students):
    subject_grades = []
    for student in students:
        grade = random.randint(3, 5)
        subject_grades.append(grade)
    return subject_grades


math_grades = grade_random(names)
history_grades = grade_random(names)
for_lang_grades = grade_random(names)
geometry_grades = grade_random(names)
chemistry_grades = grade_random(names)


data = {
    'names': names,
    'math_grades': math_grades,
    'history_grades': history_grades,
    'for_lang_grades': for_lang_grades,
    'geometry_grades': geometry_grades,
    'chemistry_grades': chemistry_grades
}
df = pd.DataFrame(data)
print(df.head())
print(f"Математика средний оценка - {df['math_grades'].mean()}, медианная оценка {df['math_grades'].median()}, отклонение отклонение {df['math_grades'].std()}")
print(f"История средний оценка - {df['history_grades'].mean()}, медианная оценка {df['history_grades'].median()}, отклонение отклонение {df['history_grades'].std()}")
print(f"Иностранный язык средний оценка - {df['for_lang_grades'].mean()}, медианная оценка {df['for_lang_grades'].median()}, отклонение отклонение {df['for_lang_grades'].std()}")
print(f"Геометрия средний оценка - {df['geometry_grades'].mean()}, медианная оценка {df['geometry_grades'].median()}, отклонение отклонение {df['geometry_grades'].std()}")
print(f"Xимия средний оценка - {df['chemistry_grades'].mean()}, медианная оценка {df['chemistry_grades'].median()}, отклонение отклонение {df['chemistry_grades'].std()}")

Q1_math = df['math_grades'].quantile(0.25)
Q3_math = df['math_grades'].quantile(0.75)

IQR = Q3_math - Q1_math


print(f"Q1 и Q3 для оценок по математике - {Q1_math}, {Q3_math}, размах IQR = {IQR}")
