calls = 0
def caunt_calls():
    global calls
    calls += 1


def string_info(string):
    caunt_calls()
    lenght = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (lenght, upper_case, lower_case)


def is_contains(string, list_to_search):
    caunt_calls()
    string_lower = string.lower()
    for item in list_to_search:
        if string_lower == item.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
