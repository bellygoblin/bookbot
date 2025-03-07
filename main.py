from stats import get_book_word_count,get_char_dict,print_book_report
import sys

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)


def main():
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  # print(text)
  number_of_words = get_book_word_count(text)
  # print(number_of_words)
  chars_dict = get_char_dict(text)
  # print(chars_dict)
  book_report = print_book_report(book_path, number_of_words, chars_dict)
  print(book_report)

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()