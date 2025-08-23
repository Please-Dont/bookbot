
def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    characters = text.lower()
    count = {}
    for char in characters:
        count[char] = count.get(char, 0) + 1
    return count

def sort_on(char):
    return char['num']

def sorted_count(count):
    sorted = []
    for char, num in count.items():
        dict = {'char': char, 'num': num}
        sorted.append(dict)
    sorted.sort(key=sort_on, reverse=True)
    return sorted
