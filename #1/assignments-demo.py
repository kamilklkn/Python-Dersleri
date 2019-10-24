x,y,z = 2,5,10

numbers = 1,5,7,10,6

# 1 - Kullanıcıdadan aldığınız iki sayısının çarpımı ile x,y,z toplamının farkı nedir?
# a = int(input('1. sayı: '))
# b = int(input('2. sayı: '))

# result = (a*b)-(x + z + y)

# 2 - y'nin x'e kalansız bölümünü hesaplayınız.
result = x//y

# 3 - (x,y,z) toplamın mod 3'ü nedir?
result = (z+z+y)%3

# 4 - y'nin x. kuvvetini hesaplayınız.
result = (y**x)

# 5 - x, *y,z = numbers işlemine göre z'nin küpü kaçtır?
numbers = 1,5,7,10,6
x, *y ,z = numbers
result = z
result = y
result = x

# 6 - x,*y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?


print(result)