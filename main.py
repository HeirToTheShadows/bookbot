def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = count_text(book_text)
    return book_text, total_words
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
def count_text(file_contents):
    total_words = 0
    word_list = file_contents.split()
    total_words = len(word_list)
    print(f"{total_words} words found in the document.")
main()