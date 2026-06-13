'''numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

new_list = [ n + 1 for n in numbers ]
print(new_list)

new_range = [ n * 2 for n in range(1,5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
names_Uppercase = [name.upper() for name in names if len(name) > 5]
print(names_Uppercase)'''

#EXERCISES
'''numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)'''

'''list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)'''

with open("./list_comprehension/files/file1.txt") as list_numbers:
    first_list = [int(n.strip()) for n in list_numbers.readlines()]

with (open("./list_comprehension/files/file2.txt") as numbers_list):
    second_list = [int(n.strip()) for n in numbers_list.readlines()]

result = [n for n in first_list if n in second_list]
print(result)