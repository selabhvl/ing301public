filename = input("Filename: ")

line_no = 1

with open(filename, 'r') as file:

    for line in file:
        print(f'{line_no:} {line}', end='')
        line_no += 1
