number_of_task_completed = 12
hours_spent = 1.5
course_name = "Python"
time_per_task = (hours_spent / number_of_task_completed)

# не разобрался, как короче сделать так, что запятая приклеилась к переменной

print("Курс:", course_name + ",", "всего задач:", str(number_of_task_completed) + ",",
      "затрачено часов:", str(hours_spent) + ",", "Среднее время выполнения:", str(time_per_task) + ".")

# разобрался в работе f - форматирования

print(f"Курс: {course_name}, всего задач: {number_of_task_completed}, "
      f"затрачено часов: {hours_spent}, Среднее время выполнения: {time_per_task}.")

print("Курс: " + course_name , "всего задач: " + str(number_of_task_completed) ,
      "затрачено часов: " + str(hours_spent) , "Среднее время выполнения: " + str(time_per_task) + ".", sep=", ")