def gcd(a, b):
    c=0
    while b != 0:
        a, b = b, a % b
        c += 1 
    print (c)
    return a

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


# Calculate and print the GCD
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
