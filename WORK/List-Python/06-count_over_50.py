# รับจำนวนตัวเลขที่จะกรอก
n = int(input())

count = 0  # ตัวนับจำนวนที่มากกว่า 50

# วนรับตัวเลข n ครั้ง
for _ in range(n):
    num = int(input())
    if num > 50:
        count += 1

# แสดงผลลัพธ์
print("จำนวนที่มากกว่า 50:", count)
