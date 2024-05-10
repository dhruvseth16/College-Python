#WAP TO PRINT SUM OF SQUARES OF FIRST N NATURAL NUMBERS
n = int(input("Enter the natural number till which to print sum of squares: "))
s = 0
for i in range(n+1):
    s += i*i
print (s)