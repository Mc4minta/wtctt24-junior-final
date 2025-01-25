# แปลง b เป็ฯ binary

b1 = 65535
b2 = 65536

print(f"b1 binary = {bin(b1)}")
print(f"b1 binary = {bin(b2)}")

# นับเลข 1 ใน binary ของ b

x1 = 0
x2 = 0

for b in str(bin(b1)):
    if(b=='1'): x1+=1
for b in str(bin(b2)):
    if(b=='1'): x2+=1

print(f"1s in b1 = {x1}")
print(f"1s in b2 = {x2}")

# หักส่วนเกินของคำตอบด้วยจำนวนเลข 1 ใน b ของแต่ละอัน แล้วเอาคำตอบมาลบกันเพื่อหา secret

c1 = 3338190210085793296455519657559881806177254504039477189883619618747088635044397372904871283091
c2 = 3338241147603304333203768006070716625461700635946153614346729157461039151388870469683278315521

# หา  secret num ด้วยวิธีหลักการที่ว่า b ห่างกันเป็นหนึ่ง

secret = (c2-x2) - (c1-x1)
print(f"secret = {secret}")