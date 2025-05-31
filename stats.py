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
def sort_ditct(char):
    #sort by value
    import operator
    sorted = dict(sorted(char.items(), key=lambda item: item [1], reverse=True))
    print(char)



   
