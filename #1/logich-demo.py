# 1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('sayı:'))
result = (sayi > 0) and (sayi >=100)
print(f'sayı 0-100 arasında mı:{result}')

# 3 - Email ve parola bilgileri ile giriş kontrolleri yapınız.
# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırın?
# 5 - Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
#     Eğer ortalama 50 ve üstünde ise geçti değil isekaldı.
#     a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#     b-) Finalden 70 aldığında ortalamanın önemi olmasın.
# 6 - Kişinin ad, kilo ve boy bilgilerini alıp kilo indexslerini hesaplayınız. 
#     Formül: (Kilo/Boy uzunluğunun karesi)
#     Aşağıdaki gruba göre kişi hangi guba girmektedir.
#     0-18.4       => Zayıf
#     18.5 - 24.9  => Normal
#     25.0 - 29.9  => Fazla Kilolu
#     30.0 - 34.9  => Şişman (Obez)
