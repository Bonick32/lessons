number_of_task_completed = 12
hours_spent = 1.5
course_name = "Python"
time_per_task = (hours_spent / number_of_task_completed)

# не разобрался, как короче сделать так, что запятая приклеилась к переменной
# сначала сделал без (+ ","), но добавлял запятую перед текстом в print(), тогда и перед запятой пробел
print("Курс:", course_name + ",", "всего задач:", str(number_of_task_completed) + ",",\
      "затрачено часов:", str(hours_spent) + ",", "Среднее время выполнения:", str(time_per_task) + ".")