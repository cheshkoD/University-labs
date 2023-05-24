# A Python function that takes two lists and returns True if they have at least one common member

list1 = list(input('Enter the 1st list: '))
list2 = list(input('Enter the 2nd list: '))

def common_letter(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result
print('Сontains at least one same value?', common_letter(list1,list2))
