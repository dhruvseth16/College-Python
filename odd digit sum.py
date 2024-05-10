n =  input("")
o = 0
while int(n)>0:
    U = int(n)%10
    if U%2==1:
        o += U
        n = int(n)//10
print(o)