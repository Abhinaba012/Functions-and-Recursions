def prime(val):
    for den in range(2,val//2+1):
        if val % den == 0:
            return "Not Prime"
    return "Prime"
    
print(list(map(prime,[11,12,13,14,15,16,17,18,19])))