number = int(input("Enter your number: ")) # รับค่าจากผู้ใช้
number = (number%2) # คำนวณเศษจากการหารด้วย 2
if(number == 0): # ถ้าเศษที่ได้เป็น 0 แสดงว่าเป็นเลขคู่
    print("เลขคู่") # แสดงว่าเป็นเลขคู่
else:
    print("เลขคี่่") # ถ้าเศษที่ได้ไม่เป็น 0 แสดงว่าเป็นเลขคี่