
print("-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-HOŞGELDİNİZ-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-")


işlem=int(input("bir işlem seçiniz    \nToplama:1\n Çıkarma:2\nÇarpma:3\nBölme:4    :  "))
sayı1=int(input("1. sayı giriniz     : "))
sayı2=int(input("2. sayı giriniz    : "))
if işlem==1:
        sonuc=(sayı1+sayı2)
        print(sonuc)
elif işlem==2:
        sonuc=(sayı1-sayı2)
        print(sonuc)
elif işlem==3:
        sonuc=(sayı1*sayı2)
        print(sonuc)
elif işlem==4 :
        if sayı2!=0:
                sonuc=(sayı1/sayı2)
                print(sonuc)
        else:
                print("hatalı işlem")
else:
        print("1,2,3,4 rakamlarından birini tıkla adamı hasta etme")
        
