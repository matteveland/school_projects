def backwards_string():
    string_1 = input('Please enter a string:')
    string_2 = input('Please enter a second string:')
    string_3= input('Please enter the thrid and final string:')

    string = [string_1, string_2, string_3]    
    string.reverse()
    backwards_string_complete = string_3 + ' ' + string_2 + ' ' +  string_1
    print('Your three strings in reverse order (concatenation) is: %s' % backwards_string_complete)
    print('Your three strings using reverse() is: %s' % string)

backwards_string()

if __name__ == '__main__' : backwards_string()
