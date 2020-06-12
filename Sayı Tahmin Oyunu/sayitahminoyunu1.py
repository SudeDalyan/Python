import random
#a aklımızdan tuttuğumuza sayı
#b bilgisayarın tahmini

print("   ")
print("ＳＡＹＩ ＴＡＨＭİＮ ＯＹＵＮＵ")
print("--------------------------------")
print("   ")

b=random.randint(0,50)
tur=0

a=int(input("0-50 arası aklınızdan bir sayı tutunuz :"))
print("Bilgisayarın tahmini :",b)

while True:
  
  if b==a:
    print("Tebrikler.")
    print(tur,". tahminde bildin.")
    break
    
  elif b<a:
    print("Daha büyük bir değer girin.")
    print("     ")
    b=random.randint(b,50)
    print("Bilgisayarın tahmini :",b)    

  else :
    print("Daha küçük bir değer girin.")
    print("     ")
    b=random.randint(0,b)
    print("Bilgisayarın tahmini :",b)
  tur+=1
