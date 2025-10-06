from stats import get_word_count
from stats import get_character_count
from stats import sort_characters

book = "books/frankenstein.txt"

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    final_text = get_book_text(book)
    final_count = get_word_count(final_text)
    final_char_count = get_character_count(final_text)
    sorted_characters = sort_characters(final_char_count)
    print(f"Found {final_count} total words")
    print(sorted_characters)
    return

main()