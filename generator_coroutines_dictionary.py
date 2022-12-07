WORDS = {}


def flatten(arr):
    for block in arr:
        for entity in block:
            yield entity


def grep(pattern):
    while True:
        sentence = yield
        if pattern in sentence:
            yield sentence


def merge(words, dct_from_add_word):
    for key in dct_from_add_word:
        if key in words:
            words[key] = merge(words[key], dct_from_add_word[key])
        else:
            words.update(dct_from_add_word)
    return words


def add_word(word):
    letter_list = list(word)
    dct_from_add_word = {}
    dictionary_two = dct_from_add_word
    for letter in letter_list:
        dictionary_two[letter] = {}
        dictionary_two = dictionary_two[letter]
    dictionary_two.update({'TERM': word})
    merge(WORDS, dct_from_add_word)
    return WORDS

list_for_get_words = []
def make_list(dictionary):
    if isinstance(dictionary, dict):
        return 1 + max(map(make_list, dictionary.values()) if dictionary else 0)
    list_for_get_words.append(dictionary)
    return 0


def get_words(chars):
    list_two = []
    make_list(WORDS)
    for word in list_for_get_words:
        if word.startswith(chars):
            list_two.append(word)
        if len(list_two) == 10:
            return list_two
    return list_two

assert list(flatten([])) == []
assert list(flatten([[]])) == []
assert list(flatten([[], []])) == []
assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
assert list(flatten([[1, 2], [3, 4, 5]])) == [1, 2, 3, 4, 5]

search = grep('bbq')
next(search)
assert search.send('Birthday invitation') is None
assert search.send('Bring bbq sauce with') == 'Bring bbq sauce with'
assert search.send('Are you hungry?') is None
assert search.send("We won't invite you to our BBQ party then") is None
assert search.send('but you better be quick (bbq) otherwise') == 'but you better be quick (bbq) otherwise'
search.close()

add_word('hello')
assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}}}}}}
add_word('hell')
assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}}}}
add_word('he')
assert WORDS == {'h': {'e': {'l': {'l': {'o': {'TERM': 'hello'}, 'TERM': 'hell'}}, 'TERM': 'he'}}}
assert set(get_words('he')) == {'he', 'hell', 'hello'}
assert get_words('l') == []
assert set(get_words('hel')) == {'hell', 'hello'}
