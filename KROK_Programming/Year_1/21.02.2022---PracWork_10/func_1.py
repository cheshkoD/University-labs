# add_Right_Digit (d, k) function,
# which is responsible for adding the digit D to the right of a positive integer K
# (D is an integer value in the range 0-9, K is an integer value).

def Add_Right_Digit(d: int, k: int):
    if not isinstance(d, int) or not isinstance(k, int):
        return None
    if not (0 <= d <= 9):
        return None

    return int(str(k) + str(d))

kx = int(input("Number k: "))
dx = int(input("Number d: "))

res = Add_Right_Digit(dx, kx)
print("Add Right Digit k: ", res)
