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
    sorted_char = []
    for character, count in char.items():
            if character.isalpha():
             alpha_dict = {"name":character,"num":count}
             sorted_char.append(alpha_dict)
    def sort_on(sorted_char):
        return sorted_char["num"]
    sorted_char.sort(reverse=True, key=sort_on) 
    return sorted_char 