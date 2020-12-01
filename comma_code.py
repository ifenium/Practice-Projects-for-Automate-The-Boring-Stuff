spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(lists):
    try: 
        if len(lists) == 1:
            return lists[0]
        else:
            return '{}, and {}'. format(', '.join(lists[:-1]), lists[-1])
    except IndexError:
        print('Index Error, you passed an empty list')

print(comma_code(spam))