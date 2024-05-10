p = int(input("Enter Principle amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter the time period: "))
a = p*(1 + r/100)**(t)
print ("Compound Interest is ", a-p)
100