num = int(input("Enter N: "))
total = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        total += i
print(f"{num} is {total}")