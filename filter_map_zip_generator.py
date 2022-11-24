list_of_words = []
LONG_TEXT = """asdlknfasldkmfasdfasdf"""


def add_word(word):
    list_of_words.append(word)
    return list_of_words.sort()


def get_words(chars):
    list_two = []
    for string in list_of_words:
        if string.startswith(chars):
            list_two.append(string)
        if len(list_two) == 5:
            return list_two
    return list_two


def crop_text(length):
    i = 0
    yield LONG_TEXT[i:length]
    for repeats in range(len(LONG_TEXT) // length):
        i += length
        yield LONG_TEXT[i:length + i]
    return 0



assert get_words('') == []

add_word('bat')
add_word('batman')

assert get_words('') == ['bat', 'batman']
assert get_words('bat') == ['bat', 'batman']
assert get_words('batm') == ['batman']
assert get_words('x') == []

add_word('bar')
add_word('bartender')
add_word('basket')
add_word('band')

assert get_words('ba') == ['band', 'bar', 'bartender', 'basket', 'bat']

text_generator = crop_text(10)
assert next(text_generator) == "asdlknfasl"
assert next(text_generator) == "dkmfasdfas"
assert next(text_generator) == "df"
