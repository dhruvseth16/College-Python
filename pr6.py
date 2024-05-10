#python program to check armstrong number
n = int(input("enter number: "))
s = 0
nstr = str(n)
for i in nstr:
    nint = int(i)
    s += nint**3

if s == n:
    print ("The given number is an Armstrong number")
else:
    print ("No, the given number is not an armstrong number")
