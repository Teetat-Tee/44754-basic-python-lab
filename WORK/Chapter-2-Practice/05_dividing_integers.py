a = int(input()) # รับค่าจำนวนเต็มจากผู้ใช้
trays = int(a / 30) # คำนวณจำนวนถาดที่ต้องใช้
remaining = a % 30 # คำนวณจำนวนที่เหลือหลังจากใช้ถาด
print("Trays: ", trays, "Remaining: ", remaining) # แสดงผลลัพธ์จำนวนถาดและจำนวนที่เหลือ
