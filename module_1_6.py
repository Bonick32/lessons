my_dict = {'Boris' : 'B.N. Ivanov', 'Lena' : 'E.F. Ivanova',
           'Fedya' : 'F.H. Haritonov', 'Zhenya' : 'E.V. Haritonova'}
print(my_dict.get('Boris', 'Такого имени нет')) # правильнее так, или можно было и без .get?
                                                # 'Такого...' убедился, как оно работает, если ключ есть
print(my_dict.get('Anton', 'Такого имени нет'))

my_dict.update({'Sasha' : 'A.S. Pushkin' , 'Kir' : 'I.V. Mozheiko'})
Kir_Bulichev = my_dict.pop('Kir')
print(Kir_Bulichev)
print(my_dict)

my_set = {True, 2, 1, 5, 'Fear', 'Kir', 5.42, 2, 5, 'Kir', False, True}
# Надо быть осторожнее во множестве с значениями True и False, если есть числа в нем
# Так как можно ошибиться, что останется, число или bool

my_set2 = {0, 2, 1, 5, 'Fear', 'Kir', 5.42, False, 2, 5, 'Kir', 0, 2, " ", ':'}
print(my_set)
print(my_set2)
my_set2.discard('Fear')
my_set2.add('Happy')
print(my_set2)