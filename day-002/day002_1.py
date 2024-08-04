ids_sum = 0

with open('input.txt', encoding='utf-8') as file:
    content = file.read()

    for i in content.split('\n'):
        game_name, cubes = i.split(':')
        cubes_splitted = cubes.split('; ')
        is_game_possible = True
        for c in cubes_splitted:
            cube = c.strip().split(', ')
            print(cube)
            for color in cube:
                number, color_name = color.split()
                print(number, color_name)
                if color_name == 'red' and int(number) > 12:
                    is_game_possible = False
                elif color_name == 'blue' and int(number) > 14:
                    is_game_possible = False
                elif color_name == 'green' and int(number) > 13:
                    is_game_possible = False

        if is_game_possible:
            ids_sum += int(game_name.split()[1])


print(ids_sum)
