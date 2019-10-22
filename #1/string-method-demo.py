website =  'https://www.a1gim.com'
course  =  "Bu bir platform web sitesidir. Güçlü işlevsel birliktelikler kurar."
message =  ' Hello World '

# 1 - " Hello World " karakter dizisinde baş ve sondaki boşlukları silin.
result  = message.strip()
result  = message.lstrip()          #Soldan boşluk silmek için
result  = message.rstrip()          #Sağdan boşluk silmek için
result  = website.lstrip('/:psth') + '\n'         #Sağdan boşluk silmek için

# 2 - "https://www.a1gim.com" karakter dizisindeki a1gim dışındaki tüm karakterleri silin.
# print(" Başlangıç:",website.find('a1gim'),"Bitiş:",len('a1gim'))
result  = website[website.find('a1gim'):website.find('a1gim')+len('a1gim')]
result = website.strip('spth./wmoc')

# 3 - course karakter dizsindeki tüm karakterleri küçük yapın
result  = course.lower()

# 4 - web sitesi içinde kaç tane m karakteri vardır
result  =   website.count('m')

# 5 - web sitesi www ile başlayıp com ile biyiyor mu?
result = website.replace('https://','')
result_start = result.startswith('www')
result_end = result.endswith('com')
if result_start==True and result_end==True :
    result = 'Web sayfası www ile başlayıp, com ile bitmekte'
else :
    result = "Web sayfası doğru kodlanmamış"

# 6 - websitesi içierisnde .com ifadesi var mı?
result = website.find('.com')
if result >=0:
    result = 'Web sayfası .com ile bitmekte'
else:
     result = 'Web sayfası doğru kodlanmamış'

# 7 - Course içindeki tüm karakterler alfabetik mi?
result = course.isalpha()
result = course.isdigit()

# 8- course ifadesini 50 karakter içine yerleştirip sağdan ve soldan * ekleyin
result = course.center(80,'*')
result = course.rjust(80,'*')
result = course.ljust(80,'/')

# 9 - course karakter dizisinde tüm boşluk karakterlerini - ile değiştirin
result = course.replace(' ','-')

# 10 - "Hello World" karakter dizisinde World kelimesini There olarak değiştirelim
result = message.replace('World','There')

# 11 - 'course' karakter disini boşluk karakterlerinden ayırın
result  = course.split(' ')

print(result)