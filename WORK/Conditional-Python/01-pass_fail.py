score = int(input("Enter your score: "))  # รับคะแนนจากผู้ใช้
if(score >= 50): # ตรวจสอบว่าคะแนนมากกว่าหรือเท่ากับ 50 หรือไม่
    print("Pass") # ถ้าคะแนนมากกว่าหรือเท่ากับ 50 ให้พิมพ์ "Pass"
else: # ถ้าคะแนนน้อยกว่า 50 ให้พิมพ์ "Fail"
    print("Fail") 