def check(n):
    if (n < 2):
        return (n % 2 ==0)
    return (check(n - 2))
n=int(input("enter number:"))
if (check(n)==True):
     print("Number is Even!")
else:
     print("Number is Odd!")
