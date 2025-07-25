from stats import get_num_words, get_chars_dict
from sys import argv, exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)
    book_path = argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    # print(chars_dict)
    for char, count in chars_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
