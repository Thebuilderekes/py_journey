# loop through the words from first to last  and store it in a variable
# loop through the word from last to first and store in a variable
# if forward_check loop and backward_checks loop is equal, word is palidrome else word is not


# def check_word(word):
#    backward_check = []
#    forward_check = []
#    for char in word:
#        backward_check.insert(0, char)
#    for char in word:
#        forward_check.append(char)
#    if backward_check == forward_check:
#        return "this is a palidrome"
#    return "not a palidrome"
#
#
# print(check_word("tacodfdcat"))
def is_palindrome(s):
    """is_palindrome function to check if word is a palidrome"""
    # Base case: if the string is empty or a single character, it's a palindrome
    if len(s) <= 1:
        return True
    # If first and last characters don't match, it's not a palindrome
    if s[0] != s[-1]:
        return False
    # Call the function recursively on the substring without the first and last characters
    return is_palindrome(s[1:-1])


print(is_palindrome("tacocatf"))
