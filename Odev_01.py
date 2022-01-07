min_sayi = int(input("Minimum Sayıyı Giriniz : \n"))
max_sayi = int(input("Maksimum Sayıyı Giriniz : \n"))
bolunecek_sayi = int(input("Bölünecek Sayıyı Giriniz : \n"))


def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunebilenler = []
    for i in range(min_sayi, max_sayi):
        kalan: int = i % bolunecek_sayi
        if kalan == 0:
            bolunebilenler.append(i)

    return len(bolunebilenler), bolunebilenler


print(bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi))
