user_input = input("Enter data: ")
temp = ""
for ch in user_input:
    if ch != "[" and ch != "]":
        temp = temp + ch
parts = temp.split(",")
main_list = []
for part in parts:
    item = part.strip()
    if item.startswith('"') and item.endswith('"'):
        item = item[1:-1]
    if item != "":
        digit_only = True
        for c in item:
            if c < '0' or c > '9':
                digit_only = False
        if digit_only:
            main_list = main_list + [int(item)]
        else:
            main_list = main_list + [item]
numbers = []
strings = []
for element in main_list:
    if type(element) == int:
        numbers = numbers + [element]
    else:
        strings = strings + [element]
count_num = 0
for n in numbers:
    count_num = count_num + 1
count_str = 0
for s in strings:
    count_str = count_str + 1
student_name = input("Enter your name: ")
name_length = 0
for letter in student_name:
    name_length = name_length + 1
if name_length % 2 == 0:
    updated_numbers = []
    position = 0
    for n in numbers:
        if position > 0:
            updated_numbers = updated_numbers + [n]
        position = position + 1
    numbers = updated_numbers
    updated_strings = []
    position = 0
    for s in strings:
        if position > 0:
            updated_strings = updated_strings + [s]
        position = position + 1
    strings = updated_strings
else:
    updated_numbers = []
    position = 0
    for n in numbers:
        if position < count_num - 1:
            updated_numbers = updated_numbers + [n]
        position = position + 1
    numbers = updated_numbers
    updated_strings = []
    position = 0
    for s in strings:
        if position < count_str - 1:
            updated_strings = updated_strings + [s]
        position = position + 1
    strings = updated_strings
print("Numbers List:", numbers)
print("Strings List:", strings)
print("Total Numbers:", count_num)
print("Total Strings:", count_str)