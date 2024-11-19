grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average_grades = list(grades) #продублировал список, чтоб не изменять начальный
average_grades[0] = sum(grades[0])/len(grades[0])
average_grades[1] = sum(grades[1])/len(grades[1])
average_grades[2] = sum(grades[2])/len(grades[2])
average_grades[3] = sum(grades[3])/len(grades[3])
average_grades[4] = sum(grades[4])/len(grades[4])
# интуиция подсказывает, что можно сократить и оптимизировать вычисление среднего значения,
# но пока не знаю как или что-то упустил

students = list(students)
students.sort()

gradebook = dict(zip(students, average_grades)) # zip где-то слышал про данный метод, но для этой задачи
                                                # честно подсмотрел в гугле

print(gradebook)