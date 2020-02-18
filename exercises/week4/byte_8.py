# Bite 8. Rotate string characters


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """

    # removes characters from left if n positive and right if n negative
    # and put them into the oposite side
    if n >= 0:
        charchange = string[:n]
        rotword = string[n:]
        rotword = rotword + charchange
    else:
        charchange = string[n:]
        rotword = string[:n]
        rotword = charchange + rotword
    return rotword


# ex: print (rotate ('julian and bob!', 100))

# string manipulation
# src: https://www.pythonforbeginners.com/basics/string-manipulation-in-python
# print word[0]          #get one char of the word
# print word[0:1]        #get one char of the word (same as above)
# print word[0:3]        #get the first three char
# print word[:3]         #get the first three char
# print word[-3:]        #get the last three char
# print word[3:]         #get all but the three first char
# print word[:-3]        #get all but the three last character
