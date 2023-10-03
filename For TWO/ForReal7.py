n = int(1000)
def test(n):
    return [i for i in range(100,n,1) if str(i) == str(i)[::-1]]

print("\nPalindromes all 3 digit: ")
print(test(n))
