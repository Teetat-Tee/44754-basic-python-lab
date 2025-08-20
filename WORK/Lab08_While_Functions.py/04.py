n = int(input("> "))
factorial = 1
original_n = n

while n > 1:
    factorial *= n
    n -= 1

print(original_n, '! =', factorial)