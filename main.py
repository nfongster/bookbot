from stats import get_num_words, get_char_count, sort_char_count
import sys


def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text


def print_sorted_letters(filepath, num_words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_tuple in sorted:
        character, count = char_tuple["char"], char_tuple["num"]
        if character.isalpha():
            print(f"{character}: {count}")


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = args[1]

    text = get_book_text(filepath)
    num_words = get_num_words(text)
    letter_count = get_char_count(text)
    sorted_letters = sort_char_count(letter_count)

    print_sorted_letters(filepath, num_words, sorted_letters)

main()