
ogrenciler = {
    '120' : {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '0 000 000 00 00', 
    },
    '125':{
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '0 532 000 00 01', 
    },
     '128':{
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '0 532 000 00 04', 
    },
}

# 1 - Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2 - Öğrenci numaraasını kullanıcıdan alıp ilgili öğrencisini gösterin.

ogrenciler = {}

number = input('Öğrenci no: ')
name = input('Öğrenci adı: ')
surname = input('Öğrenci soyadı: ')
phone = input('Öğrenci telefon: ')


ogrenciler[number] = {
    'ad'        :name,
    'soyad'     :surname,
    'telefon'   :phone  
}
result =  ogrenciler

number = input('Öğrenci no: ')
name = input('Öğrenci adı: ')
surname = input('Öğrenci soyadı: ')
phone = input('Öğrenci telefon: ')

ogrenciler.update({
    number:{
        'ad'        : name,
        'soyad'     : surname,
        'telefon'   : phone
    },
})

result =  ogrenciler
number = input('Öğrenci no: ')
name = input('Öğrenci adı: ')
surname = input('Öğrenci soyadı: ')
phone = input('Öğrenci telefon: ')

ogrenciler.update({
    number:{
        'ad'        : name,
        'soyad'     : surname,
        'telefon'   : phone
    },
})
result =  ogrenciler
print(result)
print('*'*50)

# 2 - Öğrenci numaraasını kullanıcıdan alıp ilgili öğrencisini gösterin.
ogrenciNo= input("Öğrenci No: " )
ogrenci = ogrenciler[ogrenciNo]


print(f"Aradığınız {ogrenciNo} nolu  öğrencin adı {ogrenci['ad']} soyadı: {ogrenci['soyad']} telefon numrası {ogrenci['telefon']}")