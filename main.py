from stats import get_num_words, get_char_dict, sort_ditct

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_dict(text)
    char_list= sort_ditct(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for c in char_list:
        print(f"{c['name']}: {c['num']}") 
    print(f"============= END ===============")

   

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()