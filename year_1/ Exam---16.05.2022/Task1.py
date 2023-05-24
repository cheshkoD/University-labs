# - Task 1.
# Write a program that given an array of integers determines
# if it is sorted in "ascending" order, "descending" order or "not sorted" at all.

Array_1 = [1,2,3,4,5,6,7,8,9,10]
Array_2 = [10,9,8,7,6,5,4,3,2,1]
Array_3 = [1,2,8,9,4,7,1]

def determines_array(List):
    asc = True
    desc = True

    for number in range(1, len(List)):
        if List[number] - List[number - 1] >= 0:
            asc = asc & True
            desc = desc & False
        else:
            desc = desc & True
            asc = asc & False

    if asc and not desc:
        return " - is ascending sorted"
    elif desc and not asc:
        return " - is descending sorted"
    else:
        return " - is no sorted"

print('Arr1'  ,determines_array(Array_1))
print('Arr2'  ,determines_array(Array_2))
print('Arr3'  ,determines_array(Array_3))

