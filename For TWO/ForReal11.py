x = int(input())

for l in range (1, x + 1):  
    if l > 1:  
        for i in range (2, l):  
            if (l % i) == 0:  
                break  
        else:  
            print (l)