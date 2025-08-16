def reverse_integer(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x  
    
    rev = 0
    while x > 0:
        digit = x % 10     
        rev = rev * 10 + digit  
        x = x // 10       
    
    rev = rev * sign

    if rev < -2147483648 or rev > 2147483647:
        return 0
    return rev