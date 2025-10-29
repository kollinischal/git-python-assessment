def is_palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    print("Is palindrome:", is_palindrome("radar"))