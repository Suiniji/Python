n = int(input())
def test(n):
    return [i for i in range(0,n,1) if str(i) == str(i)[::-1]]

print("\nPalindromes up to",n,"-")
print(test(n))
