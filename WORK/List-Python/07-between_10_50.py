# รับจำนวนตัวเลข
n = int(input())

numbers = []  # เก็บค่าที่อยู่ในช่วง 10-50

for _ in range(n):
    num = int(input())
    if 10 <= num <= 50:
        numbers.append(num)

# แสดงผลลัพธ์
print("ค่าที่อยู่ในช่วง 10-50:", numbers)
