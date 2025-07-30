animals = ["Cat", "Dog", "Bird", "Cat", "Bird", "Dog"]
for x in animals:
    print(x)
    if x == "Cat":
        print("Cat")
        break
for x in range(10):
    print(x)
    for y in range(10):
        print(y)
        break




for i in range(5):
    for j in range(0,i+1):
            print("*", end="")
    print('\n')