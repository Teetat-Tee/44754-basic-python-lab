age = int(input("Enter your age: "))
day = int(input("Enter the date: "))
#กำหนดตัวแปร
if(age < 13): 
    price = 100 # ถ้าอายุน้อยกว่า 13 ปี ราคา 100 บาท
elif(age >= 13 and age <= 60):
    price = 180 # ถ้าอายุระหว่าง 13 ถึง 60 ปี ราคา 180 บาท
elif(age > 60):
    price = 120 # ถ้าอายุมากกว่า 60 ปี ราคา 120 บาท
if(day == 6 or day == 7):
    print(price + 50)  # ถ้าเป็นวันเสาร์หรืออาทิตย์ เพิ่มเงิน 50 บาท
else: 
    print(price) # ถ้าไม่ใช่วันเสาร์หรืออาทิตย์ แสดงราคาเดิม