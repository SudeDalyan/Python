import random

print("   ")
print("ＳＡＹＩ ＴＡＨＭİＮ ＯＹＵＮＵ")
print("--------------------------------")
print("   ")

 
bilgisayarinTuttuguSayi=random.randint(1,100)

say=1
while True:
  benimTahminEttigimSayi=int(input("Tahmin ettiğim sayıyı gir: "))

  if benimTahminEttigimSayi==bilgisayarinTuttuguSayi:
    print(say," tahminde bildiniz")
    break
  elif benimTahminEttigimSayi>bilgisayarinTuttuguSayi:
    print("Daha küçük bir sayı dene")
    print("   ")
  else:
    print("Daha büyük bir sayı dene")
    print("     ")
  say+=1

print("Tebrikler!")