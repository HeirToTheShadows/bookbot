from stats import get_num_words, get_char_dict, sort_ditct

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_dict(text)
    dict = sort_ditct(char_count)
    print(f"============ BOOKBOT ============'\n'Analyzing book found at books/frankenstein.txt...'\n'{dict}'\n' Found {num_words} total words '\n'{dict}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()