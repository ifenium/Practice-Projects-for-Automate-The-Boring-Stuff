spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        return '{}, and {}'. format(', '.join(lists[:-1]), lists[-1])

print(comma_code(spam))