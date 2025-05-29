def get_num_words(text):
    words = text.split()
    return len(words)
def char_list(text):
    char_list = text.split()
    return char_list
def char_count(char_list):
    char_dict = {}
    for character in char_list:
        if character in char_dict:
            char_dict[character] =+ 1
    return char_dict
