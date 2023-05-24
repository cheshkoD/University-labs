import random

random_numbers_list = random.sample(range(1, 50), 10)
print(random_numbers_list)

def max_num( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

res = max_num(random_numbers_list)
print( "max elem is: ", res )
