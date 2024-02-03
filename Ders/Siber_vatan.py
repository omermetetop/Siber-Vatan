ad=" Ömer Mete"
soy_ad="Top"
yas=16
#
karsilama="Benim adım" + ad +" "+soy_ad+" "+"yaşım"+" "+ str(yas)+" "+"hoşgeldin"
print(karsilama)
#
uzunluk =len(karsilama)
print(uzunluk)#Kelimenin kaç karakterden oluştuğunu ekrana yazar
#
print(karsilama[-1]) #Kelminein sondaki  harfini verir
#
print(karsilama[4:10])#Kelminein 4-10 arasındaki kelime ve karakterleri verir
#
print(karsilama[12:25])#Cümlenin 12:25 arasındaki kelimeleri verir
#
print(karsilama[:25])#Cümlenin en baştan 25. karakterine kadar olna kelimrlri verir
#
print(karsilama[12:])#Kelminein 
#
print(karsilama[2:25:3])#Kelminein 
#
print(karsilama[:-3])#Kelminein 
#
print(karsilama[::-1])#Kelminein 
#
karsilama_upper=karsilama.upper()#BÜTÜN HARFLERİ BÜYÜK YAPAR
print(karsilama_upper)

karsilama_lower=karsilama.lower()#bütün harfleri küçük yapar
print(karsilama_lower)

karsilama_strip=karsilama.strip()#Cümlenin başındaki boşlukları silerek yazdırır
print(karsilama_strip)

karsilama_split=karsilama.split()#liste ve virgül koyarak yazdırır
print(karsilama_split)
print(karsilama_split[6])

karsilama_join="-".join(karsilama)#her 2 karakter arasına "-" koyarak yazdırır
print(karsilama_join)

karsilama_find=karsilama.find("Ömer")#Yazılan cümlede "Ömer" kelimesi geçiyormu diye bakar
print(karsilama_find)

karsilama_startswith=karsilama.startswith("n")#n ile başlayan bir kelime varmı diye bakar
print(karsilama_startswith)

karsilama_endwith=karsilama.endswith("b")#b ile biten bir kelime varmı diye bakar
print(karsilama_endwith)

karsilama_replace=karsilama.replace("Ömer Mete","Arda")#Ömer Mete  yerine Arda yazdıracak
print(karsilama_replace)

