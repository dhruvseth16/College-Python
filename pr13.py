#WAP for factorial computation
n = int(input("Enter number to find its factorial: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print ("Factorial of", n, "is", fact)