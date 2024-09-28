calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string):
    print((len(string), string.upper(), string.lower()))
    count_calls()
    return string


def is_contains(string, is_list):
    _flag = True
    for i in is_list:
        if i.lower() == string.lower():
            _flag = True
            break
        else:
            _flag = False
    count_calls()
    print(_flag)
    return


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)
