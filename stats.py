
def word_count(text):
    words = text.split()
    count = len(words)
    return count


def char_count(text):
    my_dict = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in my_dict:
            my_dict[lower_c] += 1
        else:
            my_dict[lower_c] = 1

    return my_dict

def sort_on(items):
    return items["num"]

def sort_char_count(char_counts):
    my_list = []
    for key in char_counts:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = char_counts[key]
        my_list.append(new_dict)

    my_list.sort(reverse=True, key=sort_on)
    return my_list

