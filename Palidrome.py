def is_palindrome(x):
    if x < 0:
        return False
    original = x
    rev = 0
    
    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = x // 10
    
    if rev == original:
        return True
    else:
        return False
