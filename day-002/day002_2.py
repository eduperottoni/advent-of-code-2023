powers_sum = 0

with open('input.txt', encoding='utf-8') as file:
    content = file.read()

    for i in content.split('\n'):
        minimun = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game_name, cubes = i.split(':')
        cubes_splitted = cubes.split('; ')
        for c in cubes_splitted:
            cube = c.strip().split(', ')
            print(cube)
            for color in cube:
                number, color_name = color.split()
                print(number, color_name)
                if int(number) > minimun[color_name]:
                    minimun[color_name] = int(number)

        powers_sum += minimun['red'] * minimun['green'] * minimun['blue']

print(powers_sum)