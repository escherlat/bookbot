def count_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    words = text.split()
    result = {}
    for word in words:
        for c in word:
            key = c.lower()
            if key in result:
                result[key] += 1
            else:
                result[key] = 1
    return result

def sort_on(d):
    return d["count"]

def sort_character_count(char_dict):
    sorted_list = []
    for c in char_dict:
        sorted_list.append({'char': c, 'count': char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
