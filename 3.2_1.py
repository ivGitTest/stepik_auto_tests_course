#assert abs(-42) == -42, 'Should be 42'

string = 'Привет, {}. меня зовут {}'.format('Иван', 'Игорь')
print(string)

name1, name2 = 'Антон', 'Владимир'
string2 = f'Привет, {name1}. меня зовут {name2}'
print(string2)