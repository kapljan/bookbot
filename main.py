def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of{book_path} ---")

    text = get_book_text(book_path)
    
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

    char_count = get_character_count(text)
    
    for x in char_count:
        print(f"The '{x}' character was found {char_count[x]} times")

    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_text = {}
    text = text.lower()
    characters = list(text)
    for char in characters:
        if char in char_text:
            char_text[char] += 1
        else:
            char_text[char] = 1
    
    return char_text

main()