def caesar_cipher(string, shift_amount):
    result = ""

    for i in string:
        code = ord(i) + shift_amount
        if ord(i) > 64 and ord(i) < 91:
            number = (code - 65) % 26 + 65
            result += chr(number)
        elif ord(i) > 96 and ord(i) < 123:
            number = (code - 97) % 26 + 97
            result += chr(number)
        else: 
            result += i
    return result
            
        


#a-z = 97-122
#A-Z = 65-90
