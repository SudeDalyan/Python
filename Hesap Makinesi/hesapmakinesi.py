print("Toplama işlemi için T harfine basınız.")
print("Çıkarma işlemi için E harfine basınız.")
print("Bölme işlemi için B harfine basınız.")
print("Çarpma işlemi için Ç harfine basınız.")
print("   ")
print("   ")
print("   ")

sayi1=int(input("Birinci sayıyı giriniz :"))
sayi2=int(input("İkinci sayıyı giriniz :"))
islem=input("Yapmak istediğiniz işlemi seçiniz :")
print("   ")
print("   ")
print("   ")
if islem=="T" or islem=="t":
  islem=sayi1+sayi2
  print("İşlemin sonucu :",islem)

if islem=="E" or islem=="e":
  islem=sayi1-sayi2
  print("İşlemin sonucu :",islem)  

if islem=="B" or islem=="b":
  islem=sayi1/sayi2
  print("İşlemin sonucu :",islem)

if islem=="Ç" or islem=="ç":
  islem=sayi1*sayi2
  print("İşlemin sonucu :",islem)

print("   ")
print("   ")
print("   ")

print("Başka bir işlem yapmak istiyor musunuz ?")
again=input("E                     H       :    ")
print("   ")

if again=="E" or again=="e":
  
  sayi1=int(input("Birinci sayıyı giriniz :"))
  sayi2=int(input("İkinci sayıyı giriniz :"))
  islem=input("Yapmak istediğiniz işlemi seçiniz :")
  print("   ")
  print("   ")
  print("   ")
  if islem=="T" or islem=="t":
    islem=sayi1+sayi2
    print("İşlemin sonucu :",islem)

  if islem=="E" or islem=="e":
    islem=sayi1-sayi2
    print("İşlemin sonucu :",islem)  

  if islem=="B" or islem=="b":
    islem=sayi1/sayi2
    print("İşlemin sonucu :",islem)

  else :
    islem=sayi1*sayi2
    print("İşlemin sonucu :",islem)


else:
  print("Bu programı tercih ettiğiniz için teşekkür ederim.")



