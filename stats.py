def get_num_words(text):
    words = text.split()
    return len(words)

def char_list(words):
    char_list = words.split()
    return char_list

def char_count(char_list):
    char_dict = {}
    for character in char_list:
        c = character.lower()
        if c in char_dict:
            char_dict[c] += 1
        else: char_dict[c] = 1
    return char_dict
