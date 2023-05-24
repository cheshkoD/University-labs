# - Task 2.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.

def morseEncode(x):
    if x == '1':
        return ".----"
    elif x == '2':
        return "..---";
    elif x == '3':
        return "...--";
    elif x == '4':
        return "....-";
    elif x == '5':
        return ".....";
    elif x == '6':
        return "-....";
    elif x == '7':
        return "--...";
    elif x == '8':
        return "---..";
    elif x == '9':
        return "----.";
    elif x == '0':
        return "-----";

def morseCode(s):
    for character in s:
        print(morseEncode(character), end="")

s = str(input())
print(morseCode(s))
