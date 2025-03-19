from stats import count_words, get_character_count, sort_character_count
import sys

def get_book_text(path):
    file_contents = ""
    try:
        with open(path) as f:
            file_contents = f.read()
    except Exception as e:
        return e

    return file_contents

def pretty_print(book, word_count, characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in characters:
        if c['char'].isalpha():
            print(f"{c['char']}: {c['count']}")

def main(book):
    txt = get_book_text(book)
    word_count = count_words(txt)
    word_dict = get_character_count(txt)
    sorted_list = sort_character_count(word_dict)
    pretty_print(book, word_count, sorted_list)

def help():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
if len(sys.argv) < 2:
    help()
else:
    main(sys.argv[1])