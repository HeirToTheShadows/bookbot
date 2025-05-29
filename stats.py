def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char = {}
    for c in text.lower():
        if c in char:
            char[c] += 1
        else: char[c] = 1
    return char


   
