#1) 1’den başlayarak ilk 100 doğal sayıyı ekrana yazdıran Python programını yazınız
'''
for i in range(101):
    print(i)
'''

#2) 1’den başlayarak ilk 100 doğal sayının toplamını hesaplayan ve sonucu ekrana yazdıran
#Python programını yazınız.
'''
toplam = 0
for i in range(101):
    toplam = toplam + i

print(toplam)
'''

#3) 100 ve 200 arasında 9 ile tam bölünebilen sayıları ve bunların toplamını ekrana yazdıran
#Python programını yazınız
'''
toplam = 0

for i in range(100,201):
    if i % 9 == 0:
        toplam = toplam + i
    else:
        continue
print(toplam)
'''

#4) Kullanıcıdan bir tamsayı girmesini isteyen, 1’den başlayarak girilen tamsayıya kadar olan
#sayıları ve bunların toplamını ekrana yazdıran Python programını yazınız.
'''
toplam = 0

sayi= int(input("Tamsayi: "))

for i in range(1,sayi+1):
    toplam = toplam + i


print(toplam)
'''

#5) Kullanıcıdan bir tamsayı girmesini isteyen, 1’den başlayarak girilen tamsayıya kadar olan
#sayıların küpünü örnekte olduğu gibi sırayla alt alta ekrana yazdıran Python programını yazınız. 
'''
sayi= int(input("Tamsayi: "))

for i in range(1,sayi+1):
    print(i,"kübü= ",i**3)
'''

#6) Kullanıcıdan negatif bir tamsayı girmesini isteyen, 0’dan başlayarak girilen negatif
#tamsayıya kadar olan sayıları ekrana yazdıran Python programını yazınız.

'''
sayi = int(input("Negatif Sayi:"))

for i in range(0,sayi,-1):
    print(i)
'''


#7) Kullanıcıdan iki tamsayı girmesini isteyen, bu iki tamsayı arasındaki (sınırlar dâhil) tüm
#sayıların toplamını hesaplayan ve ekrana yazdıran Python programını yazınız.
'''
sayi1 = int(input("Sayi1:"))
sayi2 = int(input("Sayi2:"))
toplam = 0

if sayi1 > sayi2:
    for i in range(sayi2, sayi1+1):
        toplam = toplam + i
else:
    for i in range(sayi1, sayi2+1):
        toplam = toplam + i
print(toplam)
'''


#8)

'''
Başlangıç = 15
Bitiş = 29
Artış miktarı = 4
15, 19, 23, 27
Toplam = 84
'''




'''
baslangic = int(input("Baslangic Sayisi:"))
bitis = int(input("Bitis Sayisi:"))
artis = int(input("Artis Sayisi:"))
toplam =0

for i in range(baslangic, bitis + 1, artis):
    print(i)
    toplam = toplam + i
print("Toplam=",toplam)
'''

#9) Kullanıcıdan iki tamsayı girmesini isteyen, birinci sayıdan ikinci sayıya kadar olan tüm
#sayıları (sınırlar dâhil) ekrana yazdıran Python programını yazınız.
'''
sayi1 = int(input("Sayi1:"))
sayi2 = int(input("Sayi2:"))


if sayi1 > sayi2:
    for i in range(sayi2, sayi1+1):
        print(i)
else:
    for i in range(sayi1, sayi2+1):
        print(i)
'''

#10) Kullanıcıdan bir tamsayı N değeri girmesini isteyen, ilk N tane tek doğal sayıyı ve bunların
#toplamını aşağıdaki örnekte olduğu gibi ekrana yazdıran Python programını yazınız.

'''
N = int(input("N sayisi:"))
toplam = 0

for i in range(1,2*N+1,2):
    print(i, end=" ")
    toplam = toplam + i

print("\nToplam:",toplam)
'''

#11) Kullanıcıdan bir tamsayı N değeri girmesini isteyen, ilk N tane çift doğal sayıyı ve bunların
#ortalamasını aşağıdaki örnekte olduğu gibi ekrana yazdıran Python programını yazınız.
'''
N = int(input("N sayisi:"))
toplam = 0

for i in range(0,2*N,2):
    print(i, end=" ")
    toplam = toplam + i
ortalama = toplam / N
print("Ortalama:",ortalama)
'''
#12) Kullanıcıdan 10 adet sayı girmesini isteyen, kullanıcının girdiği sayıların toplamını ve
#ortalamasını hesaplayıp ekrana yazdıran Python programını yazınız.

a,b,c,d,e,f,g,h,j,k = int(input("Sayilar"))

ortalama =(a + b + c + d + e + f + g + h + j + k) / 10
print(ortalama)





