liste=[1,2,3,4,5]
print(liste)
print(liste[4])
print(type(liste))

liste[4]=155

(10,20,30)
print(liste[4])

alt_liste= liste[2:4]
print(alt_liste)

tuple=(10,20,30,40)
print(tuple)

#tuple[1]=50
#print[tuple]
alt_tuple=tuple[1:4]
print(alt_tuple)

#kumeler
kume = {100,200,300,400,500,"durukan"}
print(kume)
kume.add(700)
print(kume)
kume.update([400,900])
print(kume)

#dict dictionary sözlük 

dict = {"anahtar1":"deger1","anahatar2":"deger2"}
print(dict)

deger = dict["anahtar1"]
print(deger)

# dict=set(dict)
# print(dict)

kume=list(kume)
print(kume)


key1=list(dict.keys())
key2=list(dict.values())
print(key1,key2)

list_keys = list(dict.keys())
print(type(list_keys))
print(list_keys)

list_values = list(dict.values())
print(type(list_values))
print(list_values)

sayilar = [10,8,5,3,15]
en_buyuk=max(sayilar)
print(en_buyuk)
en_kuçuk=min(sayilar)
print(en_kuçuk)
sayilar.append(20)#kümeye parantez içine girilen sayıyı ekler
sayilar.append(99)
yeni_en_buyuk=max(sayilar)#en büyük sayıyı verir
yeni_en_kuçuk=min(sayilar)#en küçük sayıyı verir
print(yeni_en_buyuk)
print(yeni_en_kuçuk)
print(sayilar)

sayilar.pop()#verilen kümedeki en sondaki terimi yazdırır
print(sayilar)

sayilar.sort()#küçükten büyüğe yazmak için
print(sayilar)

sayilar.reverse()#tersten yazmak için
print(sayilar)

print(sayilar.count(10))#içerisinde kaçtane olduğunu gösterir

aralik=range(1,100)#son girilen sayıyı vermez buradaki 100 gibi
print(list(aralik))

import random

rastgele_sayi= random.randint(1,100)#1 ile 100 arasında rastgele bir sayı verir
print("tutulan sayı :",rastgele_sayi)

import random 

rastgele_sayi2 =random.randint(1,1000)
print("tutulan sayı " ,rastgele_sayi2)#1 ile 1000 arasında rqastgele bir sayı verir





