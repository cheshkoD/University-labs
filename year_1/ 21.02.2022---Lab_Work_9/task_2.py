# Implement a function whose parameters are two numbers and a string.
# It returns the concatenation of the string with the sum of the numbers.

def function(a:int, b:int, c:str):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, str):
        return None
    x = str(int(a)+int(b))
    return c + x

res = function(11, 4, "example")
print(res)