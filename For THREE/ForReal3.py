a = 5
b = 50
for l in range (a, b + 1):  
    if l > 1:  
        for i in range (2, l):  
            if (l % i) == 0:  
                break  
        else:  
            print (l)