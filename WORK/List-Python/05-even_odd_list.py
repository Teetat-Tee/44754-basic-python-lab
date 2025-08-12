# รับจำนวนตัวเลขที่จะกรอก
n = int(input())

even_list = []  # เก็บเลขคู่
odd_list = []   # เก็บเลขคี่

# วนรับตัวเลข n ครั้ง
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

# แสดงผลลัพธ์
print("เลขคู่:", even_list)
print("เลขคี่:", odd_list)
