def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    letter_dict = {}
    for word in text.split():
        for letter in word.lower():
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict


def sort_char_count(letter_dict):
    letter_list = []
    for key in letter_dict:
        letter_list.append({ "char": str(key), "num": letter_dict[key] })
    
    def sort_on(dict):
        return dict["num"]
    
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list