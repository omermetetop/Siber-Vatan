def faktöryel(a):
    f_sonuc=1
    for i in range(0,a):
        f_sonuc*=i+1
    print(f_sonuc)
    return f_sonuc
faktöryel()

def faktöryel2(n):
    if n == 0:
        return 1
    else:
       return n*faktöryel2(n-1)
sayi=4
print(faktöryel2(sayi))


#print(a)#name error
int("a15")#ValueError
print(10/0)#ZeroDivisionError
#print("hello"world)#syntax Error

try:
        x=int(input("x giriniz:"))
        y=int(input("y giriniz: "))
        print(x/y)
except ZeroDivisionError:
        print("sıfıra bölme hatası!")
except ValueError:
        print("x ve y için sayısal bir değer giriniz!")
except NameError:
    print("tanımlanmama hatası")
except SyntaxError:
    print(" tırnak işaretini unutma")
except Exception as ex:
    print("bilgiler yanlış ",ex)
finally :
    print("calm dawn bayb it is quality")

import re
def parola_kontrol(parola):
    if len(parola)<8:
        raise Exception ("parola uzunluğu en az 8 olması gerekmektedir!") 
    elif not re.search("[a,z]",parola):
        raise Exception("parola küçük harf içermek zorundadır!") 
    elif not re.search("[A,Z]",parola):
        raise Exception("parola buyuk harf içermek zorundadır")
pasword="12345678aZ"

try:
    parola_kontrol(pasword)
except Exception as ex:
    print(ex)
else:
    print("parola oluşturma başarılı")
