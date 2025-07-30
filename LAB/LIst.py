Num = int(input('Enter your loop'))
NumTotal = []
for i in range(Num):
    data = int(input('Enter Your Data: '))
    NumTotal += [data]
print(NumTotal)
NumTotal.sort()
print(NumTotal)