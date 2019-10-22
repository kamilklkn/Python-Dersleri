# 1 - "Bmv, Mercedes, Opel, Mazda" elamanlarına ait listeyi oluşturun.
list = ['Bmv', 'Mercedes', 'Opel', 'Mazda']
result = list

# 2 Liste kaç elamanlıdır?
result = len(list)

# 3 Listenin ilk ve son elemanı nedir?
result  = list[:1]
result2 = list[len(list)-1:]
result  =  result + result2

# 4 Mazda değerini toyota ile değiştirin
result  = list[-1] = "Toyota"

# 5 Mercedes litesnin bir elemanımıdır?
result  =  list.index('Mercedes')
if result>0:
    result = "Mercedes liste elemanı"
else :
    result = "Mercedes liste elemanı değil"

result = 'Mercedes' in list

# 6 Listenin -2 indeksindeki değer nedir?
result = list[-2]

# 7 Listenin ilk 3 elamanını alın
result = list[:3]

# 8 Listenin son 2 elamanını alın
result = list[len(list)-2:]

# 9 Listenin üzerine Audi ve Nissan ekleyin
list + ['Audi','Nissan']
result = list + ['Audi','Nissan']

# 10 Lİstenin son elemanını silin.
result  = list.pop(len(list)-1) 
result  = list

del list[-1]
result = license

# 11 Listenin elemanlarını tersten yazdırın.
result =list[::-1]

list.sort(reverse=True)
result = list

# 12 Aşağıdaki verileri bir liste içersinde saklayın.
    # studentA: Yiğit Bilgi 2010,(70,80,30)
    # studentB: Sena Turan 1991,(80,80,70)
    # studentC: Ahmet Turan 1998,(80,80,90)

studentA =['Yiğit','Bilgi', 2010, [70,80,30]]
studentB =['Sena','Turan', 1991,  [80,80,70]]
studentC =['Ahmet','Turan', 1998, [80,80,90]]

student_list = studentA + studentB + studentC
result = student_list

# 13 Liste elemanlarını ekrana yazdırınız.
result = studentA[0] +' '+ studentA[1] +' '+ str(studentA[2])
result = f"{studentA[0]} {studentA[1]} {2019 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/2}"



print(result)