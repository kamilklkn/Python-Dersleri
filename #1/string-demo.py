wesite = "http://www.a1gim.com"
course = "Ortaklıklar Kurar: Stratejik ortaklıklar kurar."

# 1 - 'course' karakter dizisinde kaç karakter bulunmaktadır
print("1 --------","\n")
print("Karakter Sayısı:",len(course),"\n")

# 2 - 'website' içinden www karakterlerini alın
print("2 --------","\n")
print("www Karakterleri:",wesite[7:10],"\n")

# 3 - 'Website' içinden com karakterlerini alın
print("3 --------","\n")
lenght = len(wesite)
print(wesite[(lenght-3):])

# 4 - 'course' içinden ilk 15 ve son 15 karakterlerini alın
print("4 --------","\n")
lenght = len(course)
print("İlk 15 Karakter:", course[0:15],"\n","Son 15 Karakter:", course[(lenght-15):])

# 5 - 'course' ifadesindeki karakterleri tersten yazdırın.
print("\n","5 --------","\n")
print(course[::-1])

name, surname, age, job ='Bora', 'Yılmaz', 23, 'Mühendis'
# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
print("6 --------","\n")
print("Benim adım {} {}, yaşım {} ve mesleğim {}.".format(name, surname,age,job))

# 7 - "Hello World" ifadesindeki w harfini 'W' ile değiştirin.
print("7 --------","\n")
S = 'Hello World'
S = S[0:6] + 'W'+ S[-4:]
print(S)
S.replace('w','W')
print(S)

# 8 - 'abc' ifadesini yan yana 3 defa yazdırın.
print("8 --------","\n")
s = 'abc' * 3
print(s)
