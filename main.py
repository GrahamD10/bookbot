from stats import word_counter
from stats import char_counter
from stats import sort_dict
import sys


def get_book_text(book_file_path):
    with open(book_file_path) as f:
        book_text = f.read()
    return book_text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num = word_counter(book_text)
    char_count = char_counter(book_text)
    sorted_chars = sort_dict(char_count)



    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
    