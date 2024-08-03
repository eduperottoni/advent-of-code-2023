total = 0

with open('input.txt', encoding='utf-8') as file:
    for i in file.read().split('\n'):
        number = ''
        for j in i:
            if j.isdigit():
                number += j
                break
        for j in reversed(i):
            if j.isdigit():
                number += j
                break
        total += int(number)

print(total)
