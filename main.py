# Module 3 Practice 1

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list_1 = [len(string), string.upper(), string.lower()]
    return list_1

def is_contains(string: str, list_to_search: list):
    count_calls()
    list_to_search = [item.lower() for item in list_to_search]
    return string.lower() in list_to_search

print(string_info('Коянискацци'))
print(string_info('Casino Royal'))
print(is_contains('red', ['Banana', 'Pineapple', 'Red Alert']))
print(is_contains('alert', ['Banana', 'Pineapple', 'Red Alert']))
print(is_contains('red alert', ['Banana', 'Pineapple', 'Red Alert']))
print(is_contains('Street Fighter', ['street', 'fight', 'fighter']))
print(is_contains('Say Something', ['say', 'something', 'goodbye']))
print(calls)