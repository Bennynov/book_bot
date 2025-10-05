book = "books/frankenstein.txt"
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    final_text = get_book_text(book)
    print(final_text)
    return


main()