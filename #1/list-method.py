numbers = [1,10,5,16,4,9,10]
latters = ['a','g','s','b','y','a','s']

val = min(numbers)      #Dizin en büyük değerini getir
val = max(numbers)      #Dizin en küçük değerini getir
val = min(latters)      #Dizin ilk harfini getirir
val = min(latters)      #Dizin alfabetik son harfini getirir 

val = numbers[3:6]
val = numbers[:3] 

numbers[4] = 40         #Dizenin 4 değerini 40 değeri ile değiştirir.
numbers.append(60)      #Dizinin sonuna 60 rakımını ekler
numbers.insert(3, 78)   #Dizinin 3 dzesindeki değeri 78 ile değiştir
numbers.insert(-1,67)   #Dizinin sonuna 60 değerini değiştir
numbers.pop()           #Dizinin son indeksini siler
numbers.pop(3)          #Dizinin 3. indeksini siler
numbers.remove(67)      #Dizinin içinde 59 bulur ve siler

numbers.sort()          #diziyi numerik olarak sıralar
numbers.reverse()       #diziyi numerik ters çeviri

numbers= numbers.count(10)
# numbers.clear()

print(numbers)

markalar    =   []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")

markalar.append(markalar)
markalar.append(marka)

marka = input("marka: ")
markalar.append(markalar)
markalar.append(marka)


print(marka)