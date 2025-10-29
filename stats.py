def word_counter(full_text):
    words = full_text.split()
    word_count = len(words)
    return word_count

def char_counter(full_text):
    char_dict = {}
    lower = full_text.lower()
    text_list = list(lower)
    
    for char in text_list:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_dict(char_dict):
    sorted_dict = []
    for char, num in char_dict.items():
        if char.isalpha():
            sorted_dict.append({"char":char, "num":num})

    # python
    for entry in sorted_dict:
        assert isinstance(entry, dict), entry

    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict


