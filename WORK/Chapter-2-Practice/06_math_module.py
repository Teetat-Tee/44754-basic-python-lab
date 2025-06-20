import math

# รับข้อมูลจากผู้ใช้
x1, y1, x2, y2 = map(int, input().split())

# คำนวณระยะทาง
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# แสดงผลลัพธ์
print(distance)
