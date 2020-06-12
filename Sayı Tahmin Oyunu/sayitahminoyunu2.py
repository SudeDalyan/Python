import random

print("   ")
print("ＳＡＹＩ ＴＡＨＭİＮ ＯＹＵＮＵ")
print("--------------------------------")
print("   ")

EnKucukDeger=1
EnBuyukDeger=100
cevap="h"
while cevap!="e":
  print("enkücük={} , enbüyük={}".format(EnKucukDeger,EnBuyukDeger))
  bilgisayarinTahminEttigiSayi=random.randint(EnKucukDeger,EnBuyukDeger)
  cevap=input("{} senin tuttuğun sayı mı? [e]vet / daha [b]üyük olmalı / [k]üçük olmalı: ".format(bilgisayarinTahminEttigiSayi))
  if cevap=="e":
    print("Bildim")
  elif cevap=="b":
    EnKucukDeger=bilgisayarinTahminEttigiSayi+1
  else:
    EnBuyukDeger=bilgisayarinTahminEttigiSayi-1

  