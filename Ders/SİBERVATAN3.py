meyveler=["elma","armut","limon","şeftali"]
print(meyveler[2])# burada limon çıktısını verir

sayılar=[10,20,30,40,50]
toplam=0            
for sayı in sayılar:
    toplam+=sayı
print(toplam)

meyveler=["elma","armut","limon","şeftali"]

for meyve in meyveler:
    print(meyve)

sayilar=[2,3,4,5,6,7,8,9,98,87,76,65,54,43,32]
for tek in sayilar:
    if tek%2!=0:
       print("tek: ",tek)
    else:
        print("çift:",tek)

sayı=int(input("bir sayı giriniz:"))

sayac=0

while sayac<=sayı:
    print(sayac)
    sayac+=1    

say1=int(input("bir sayı giriniz:"))    
say2=int(input("bir sayı giriniz:")) 
say3=int(input("bir sayı giriniz:")) 
say4=int(input("bir sayı giriniz:")) 
say5=int(input("bir sayı giriniz:")) 

liste=[]

liste.append(say1)
liste.append(say2)
liste.append(say3)
liste.append(say4)
liste.append(say5)

print(liste)

liste = []
i = 1

while i <= 5:
    sayi = int(input(" sayı giriniz: "))
    liste.append(sayi)
    i += 1

print("Girilen sayılar:", liste)



