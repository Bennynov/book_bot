
def get_word_count(text):
    split_text = text.split()
    word_count = 0
    for i in split_text:
        word_count += 1
    return word_count
        