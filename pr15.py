#wap to print reverse of a number
n = input("Enter the number to reverse: ")
l1 = []
lr = []
for i in n:
    l1.append(i)

for k in range(len(l1)):
    y = l1.pop()
    lr.append(y)

print ("Reverse of the number is: ",''.join(lr))