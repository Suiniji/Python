
name = str(input("What is your name?"))
con = name.count("a")

if con > 2:
    print("higher than 2 letter `a`")
else:
    print("Lower or equal to 2 letter `a`")