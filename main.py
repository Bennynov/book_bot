from stats import get_word_count
book = "books/frankenstein.txt"

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    final_text = get_book_text(book)
    
    final_count = get_word_count(final_text)
    print(f"Found {final_count} total words")
    return

main()