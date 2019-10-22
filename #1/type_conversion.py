# Consoldan veri alalım
x = input ('1 Sayı..')
y = input ('2 Sayı..')

# Aldığımız veriyi ekrana yazdıralım
print("")
print("1 Sayı:", type(x), x)
print("2 sayı:", type(y), y)
print(" ")

#Toplama işlemini yapmadan önce int tipie dönüştürelim
total = int(x) +int(y)

#Toplam değeri yazdıralım
print("Toplam:",total)
print("////////////////////////////////////////// ")

x = 5              #int 
y = 2.5            #float 
name = 'Çınar'     #string     
isOnline = True    #bool

print(type(x), type(y), type(name),type(isOnline))
