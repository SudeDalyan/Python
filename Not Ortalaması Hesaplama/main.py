input("Öğrenci numaranızı giriniz :")
vize=int(input("Lütfen vize notunuzu giriniz :"))
final=int(input("Lütfen final notunuzu giriniz :"))
ortalama=(vize+final)/2
print("Ortalamanız :",ortalama)



if final<50:
  print("Final notunuz 50'nin altında.Ders tekrarı.") 
  
else :

    if ortalama<=100 and ortalama>=90  :
      print("Harf notunuz AA.")
      print("Dersi başarıyla tamamladınız.") 

    elif ortalama<=89 and ortalama>=80 :
     print("Harf notunuz BB.") 
     print("Dersi başarıyla tamamladınız.") 

    elif ortalama<=79 and ortalama>=70 : 
     print("Harf notunuz DD.")
     print("Dersi başarıyla tamamladınız.")

    elif ortalama<=69 and ortalama>=60 : 
     print("Harf notunuz CC.")
     print("Dersi başarıyla tamamladınız.")

    elif ortalama<=59 and ortalama>=50 : 
     print("Harf notunuz DD.")
     print("Dersi başarıyla tamamladınız.")
    
    else:
      print("Harf notunuz FF.")
      print("Ders tekrarı.") 
