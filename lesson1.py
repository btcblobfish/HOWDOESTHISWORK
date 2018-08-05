def reverse(string): #function to reverse string#
    length = len(string)-1 #get string length-1, position of the rightmost letter#
    while length >= 0: #while the string length is greater than or equal to 0, print out string[length]#
        print(string[length]) #print letter at rightmost position#
        length = length-1 #decrease the "length" to move to next spot to the left#

reverse('Shower')

def palindrome(vari):
    new_vari = vari[::-1] #simpler way to get the string backwards cool
    return new_vari==vari

palindrome('racecar')