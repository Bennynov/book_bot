def get_word_count(text):
    split_text = text.split()
    word_count = 0
    for i in split_text:
        word_count += 1
    return word_count

def get_character_count(text):
      character_dict = {}
      lower_case_text = text.lower()
      for ch in lower_case_text:
          if ch not in character_dict:
                character_dict[ch] = 0
          character_dict[ch] += 1
      return character_dict
      