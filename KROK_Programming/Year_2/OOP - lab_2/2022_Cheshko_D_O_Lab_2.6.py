def test(num):
    ones = bin(num).replace("0b", "").count('1')

    return "Number of ones in binary presented: " + str(ones)

n = int(input("Enter positive number: "))
print("in binary: ",bin(n))
print(test(n))
