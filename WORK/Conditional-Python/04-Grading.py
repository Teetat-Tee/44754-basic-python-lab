a = int(input()) # รับค่าคะแนนเก็บ
b = int(input()) # รับค่าคะแนนสอบกลางภาค
c = int(input()) # รับค่าคะแนนสอบปลายภาค
score = a + b + c # คำนวณคะแนนรวม
if(score >= 80): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 80
    print("A") # ให้พิมพ์ "A"
elif(score >= 75 and score < 80): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 75 และน้อยกว่า 80
    print("B+") # ให้พิมพ์ "B+"
elif(score >= 70 and score < 75): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 70 และน้อยกว่า 75
    print("B") # ให้พิมพ์ "B"
elif(score >= 65 and score < 70): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 65 และน้อยกว่า 70
    print("C+") # ให้พิมพ์ "C+"
elif(score >= 60 and score < 65): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 60 และน้อยกว่า 65
    print("C") # ให้พิมพ์ "C"
elif(score >= 55 and score < 60): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 55 และน้อยกว่า 60
    print("D+") # ให้พิมพ์ "D+"
elif(score >= 50 and score < 55): # ถ้าคะแนนรวมมากกว่าหรือเท่ากับ 50 และน้อยกว่า 55
    print("D") # ให้พิมพ์ "D"
elif(score <= 49): # ถ้าคะแนนรวมต่ำกว่าหรือเท่ากับ 49
    print("F") # ให้พิมพ์ "F"
