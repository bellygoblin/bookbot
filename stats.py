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
  characters = []

  for char in char_dict:
    new_char_dict = {}
    new_char_dict["letter"] = char
    new_char_dict["count"] = char_dict[char]
    characters.append(new_char_dict)
  characters.sort(reverse=True, key=sort_on)

  print(f"--- Begin report of {book_path}")
  print(f"Found {word_count} total words")
  for item in characters:
    print(f"{item["letter"]}: {item["count"]}")
  print("--- End report ---")  

def sort_on(dict):
  return dict["count"]