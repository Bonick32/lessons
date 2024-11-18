immutable_var = 1, 2, True, "Forgot"
print(immutable_var)

# immutable_var[0] = 22 Данная операция невозможна из-за того,
#                       что элементы, содержащиеся в кортеже - неизменяемы
#                       проще говоря, Кортеж - неизменяемый объект

mutable_list = [56, 1, "Text", False, 8, "2 Text"]
mutable_list.append(6)
mutable_list[2] = 2
mutable_list[3] = True
print(mutable_list)
