# รับจำนวนตัวเลขที่จะกรอก
n = int(input())

total = 0  # ตัวแปรเก็บผลรวม

# วนรับตัวเลข n ครั้ง
for _ in range(n):
    num = int(input())
    total += num

# แสดงผลรวม
print("ผลรวม:", total)
