'''numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

new_list = [ n + 1 for n in numbers ]
print(new_list)

new_range = [ n * 2 for n in range(1,5)]
print(new_range)'''

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
names_Uppercase = [name.upper() for name in names if len(name) > 5]
print(names_Uppercase)