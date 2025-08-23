import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

from stats import get_num_words
from stats import get_character_count
from stats import sorted_count

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def main():
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    character_count = get_character_count(book_text)
    sorted_characters = sorted_count(character_count)
    for char in sorted_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
main()