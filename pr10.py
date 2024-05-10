#WAP TO PRINT SUM OF cubes OF FIRST N NATURAL NUMBERS
n = int(input("Enter the natural number till which to print sum of cubes: "))
s = 0
for i in range(n+1):
    s += i*i*i
print (s)   