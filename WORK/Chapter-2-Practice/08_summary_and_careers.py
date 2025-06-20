price = int(input()) #ใส่ราคาอาหาร
tip = int(input()) #ใส่เปอร์เซ็นต์ทิป
people = int(input()) #ใส่จำนวนคนที่จะแบ่งจ่าย
total = (price + (price * tip / 100)) / people #คำนวณหาราคาอาหารรวมกับทิปแล้วหารจำนวนคน
print("Each person pays: ", total) #แสดงผลลัพธ์ที่แต่ละคนต้องจ่าย