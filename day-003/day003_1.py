sum = 0


with open('input.txt', encoding='utf-8') as file:
    content = file.read()
    loc_dict = {}
    for i, line in enumerate(content.split('\n')):
        for j, char in enumerate(line):
            if char != '.':
                loc_dict[(i, j)] = char

    print(loc_dict)
