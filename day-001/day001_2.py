numbers_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def search_key_on_string(string: str) -> tuple[bool, str | None]:
    for key in numbers_dict:
        if key in string:
            return True, key
    return False, ''

total = 0
with open('input.txt', encoding='utf-8') as file:
    content = file.read()
    temp_digit = ''
    for i in content.split('\n'):
        number = ''
        for j in i:
            if j.isdigit():
                number += j
                break
            temp_digit += j

            result = search_key_on_string(temp_digit)
            if result[0]:
                number += numbers_dict[result[1]]
                temp_digit = ''
                break
        for j in reversed(i):
            if j.isdigit():
                number += j
                break
            temp_digit = f'{j}{temp_digit}'
            result = search_key_on_string(temp_digit)
            if result[0]:
                number += numbers_dict[result[1]]
                temp_digit = ''
                break

        total += int(number)

print(total)