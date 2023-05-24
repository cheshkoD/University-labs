# Implement a script which works the same as str.split
#   Note:
#   Usage of str.split method is prohibited

def my_split(s, sep=' '):
    s = s.lstrip(sep)
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = my_split(s[pos+1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]

print (my_split(input('Enter the sentence: ')))