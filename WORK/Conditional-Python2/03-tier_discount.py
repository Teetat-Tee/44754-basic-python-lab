price = float(input("enter your price: ")) #รับค่า
if(price >= 2000): 
    print(price * 0.85) # ถ้าราคา 2000 บาทขึ้นไป ให้ส่วนลด 15%
elif(price >= 1000 and price < 2000):
    print(price * 0.90) # ถ้าราคา 1000 ถึง 1999 บาท ให้ส่วนลด 10%
elif(price >= 500 and price < 1000):
    print(price * 0.95) # ถ้าราคา 500 ถึง 999 บาท ให้ส่วนลด 5%
elif(price <= 500):
    print(price) # ถ้าราคาไม่ถึง 500 บาท ไม่ให้ส่วนลด