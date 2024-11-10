def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  # print(text)
  number_of_words = get_book_word_count(text)
  # print(number_of_words)
  chars_dict = get_char_dict(text)
  print(chars_dict)
  # book_report = print_book_report(chars_dict)
  # print(book_report)

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def get_book_word_count(book_text):
  word_count = 0
  words = book_text.split()
  for word in words:
    word_count += 1
  return word_count
  
def get_char_dict(book_text):
  char_dict = {}
  for char in book_text:
    lowered_char = char.lower()
    if lowered_char.isalpha() and lowered_char in char_dict:
      char_dict[lowered_char] += 1
    elif lowered_char.isalpha():
      char_dict[lowered_char] = 1
  return char_dict

def print_book_report(book_path, word_count, char_dict):
  print(f"--- Begin report of {book_path}")
  print(f"{word_count} words found in the document")


main()