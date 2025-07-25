def get_sum(a,b):
    #good luck!
    if a < b:        
        c = b-a-1
        suma = 0
        for num in range(c):
            numm = num+1
            resta = b-numm
            suma = suma + resta
        return suma + a + b
    if a > b:
        c = a - b - 1
        suma = 0
        for num in range(c):
            numm = num+1
            resta = a-numm
            suma = suma + resta
        return suma + a + b
    if a == b:
        return a            
    

print(get_sum(-1,2))

