a = int(input())
b = int(input())
c = int(input())
# รับค่าตัวเลขสามตัวจากผู้ใช้และหาค่ามากที่สุด
if(a > b and a > c): # ถ้า a มากที่สุด
    print(a) # แสดงผลลัพธ์ a
elif(b > a and b > c): # ถ้า b มากที่สุด
    print(b) # แสดงผลลัพธ์ b
elif(c > a and c > b): # ถ้า c มากที่สุด
    print(c) # แสดงผลลัพธ์ c