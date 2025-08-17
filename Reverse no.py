def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = int(str(x)[::-1]) * sign
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num

print(reverse(123))  
print(reverse(-123))  
print(reverse(120)) 
