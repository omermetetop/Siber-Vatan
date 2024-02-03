#soru 1
cumle=input("bir cümle giriniz :")

cumle_strip=cumle.strip()

cumle_lower=cumle_strip.lower()
print(cumle_lower) 

#soru 2

karakter="merhaba ben ömer. ömer yazılım la ilgilenir. yazılım güzeldir"
print(karakter.count("ömer"))

#soru 3

kelime = input("bir kelime girin : ")
harf = input("bir harf girin : ")
print(kelime.count(harf))

#soru 4

Motor = "YAMAHA"  
Araba = "BMW"

cumle = "benim sevdğim motor "+ Motor +" benim sevdiğim araba ise "+ Araba

print(cumle[5:20])

#soru 5
cumle = input("Lütfen bir cümle girin: ")
kelimeler = cumle.split()
sirali_kelimeler = sorted(kelimeler)
for kelime in sirali_kelimeler:
    print(kelime)




#soru 6 

string1=input("adınızı büyük harflerle giriniz :")
string2=input("yaşınızı büyük harflerle giriniz :")

cumle2= (string1 + " " + string2)
cumle2_lower=cumle2.lower()
print(cumle2_lower)

#soru 7
string ="Merhaba benim adım ömer ve şuan siber vatan ödevimi yapıyorum"

yeni_string = string.replace("ömer","mete")

print(yeni_string)





#soru 8

kelime=input("içinde a harfi bulunan bir kelime girin")
kelime_replace=kelime.replace("a","@")
print(kelime_replace)#Girilen kelimedeki a harfini @ işareti değiştirir 


#soru 9

kelime1 = input("bir kelime girin:")
kelimenin_tersi = kelime1[::-1]

if kelime1 == kelimenin_tersi:
    print("palindromedur")
else:
    print("palindrom değildir")
    


#soru 10
    
cumle=input("bir cümle giriniz")

cumledeki_kelimeler=len(cumle)
print(cumledeki_kelimeler.max())

#soru 11

liste=[1,2,3,4,5,6,7,8]
liste_uzunluk=len(liste)

oratdaki=liste_uzunluk//2
print(oratdaki)


#soru 12

tuple = ("yamaha","honda","cf moto","suzuki","kawasaki","ducati")
yeni_tuple = tuple[1:3]
print(yeni_tuple)

#soru 13

set={1,2,3,4,5,6,7,8,9}
set.add(10)
print(set)

set.remove(10)
print(set)


#soru 14

dict={"Yamaha":"R1M","BMW":"S1000RR"}



dict.update({"Honda":"CBR 1000 RR"})

dict.pop("Yamaha")

print(dict)

#soru 15

sayilar = [1,2,3,4,5,7]
yeni_sayi = 6
orta_index = (len(sayilar) // 2) if len(sayilar) % 2 == 0 else (len(sayilar) - 1) // 2
sayilar.insert(orta_index, yeni_sayi)
print(sayilar)


#soru 16
sayilar = [1,2,3,4,5]
ortadaki_index = (len(sayilar) // 2) if len(sayilar) % 2 == 0 else (len(sayilar) - 1) // 2
ort_eleman = tuple((sayilar[ortadaki_index],))
print(ort_eleman)

#soru 17


sayilar = {1, 2, 3, 4, 5}
liste = list(sayilar)
toplam = sum(liste)
print(toplam)


#soru 18 

