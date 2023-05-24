#creating values
a = 10
b = 50

#swapping values using bitwise operations
# " ^ " - mean XOR operator
tt = a^b
a = tt^a
b = tt^b

#checking result
print("Value of a:", a)
print("Value of b:", b)