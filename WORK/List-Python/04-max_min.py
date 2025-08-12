# รับจำนวนข้อมูล
n = int(input())

numbers = []  # สร้างลิสต์เก็บตัวเลข

# วนรับตัวเลข n ครั้ง
for _ in range(n):
    num = int(input())
    numbers.append(num)

# แสดงค่ามากที่สุดและน้อยที่สุด
print("มากที่สุด:", max(numbers))
print("น้อยที่สุด:", min(numbers))
