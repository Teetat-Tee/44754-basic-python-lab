n = int(input()) #รับจำนวนเต็มบวก 
numb = []
for _ in range(n):
    num = int(input()) #รับตัวเลข
    numb.append(num) #เพิ่มลงใส่ลิส
print("ลิสตเดิม: ",numb)

numb.sort(reverse=False)

print("ลิสตเรียงแล้ว: ", numb)