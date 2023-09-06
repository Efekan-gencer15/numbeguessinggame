import random 
import time


print ("""
       ******************** 
        Sayı Tahmin Oyunu
       
       1 ile 40 Arasındaki Sayıyı Tahmin Edin!
       ********************
    """)

rastgele_sayı = random.randint(1,40)

tahmin_hakkı = 7

while True:
    tahmin = int(input("Tahmininiz:"))

    if (tahmin < rastgele_sayı):
        print ("Bilgiler Sorgulanıyor ...")
        time.sleep(1)
        print ("Daha Yüksek Bir Sayı Giriniz" )

        tahmin_hakkı -= 1
        print("Kalan Tahmin Hakkınız:",tahmin_hakkı)
    elif (tahmin > rastgele_sayı):
        print ("Bilgiler Sorgulanıyor ...")
        time.sleep(1)
        print ("Daha Düşük Bir Değer Giriniz" )
        tahmin_hakkı -= 1
        print("Kalan Tahmin Hakkınız :",tahmin_hakkı)
    else:
        print("Bilgiler Sorgulanıyor ...")
        time.sleep(1)
        print("Tebrikler !!! Sayımız ",rastgele_sayı )
        break

    if (tahmin_hakkı ==0):
        print("Tahmin Hakkınız Bitti !!!")
        print ("Sayımız : ", rastgele_sayı)
        break



            





