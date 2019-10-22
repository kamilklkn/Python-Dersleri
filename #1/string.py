
name = 'Sadık'
surname = 'Turan'
age = 36

greeting='My name is '+ str(name ) + ' ' + str(surname) + ' and \n I am ' + str(age) + ' years old.'
length = len(greeting)

print(greeting)
print("Birinci Karakteri Yaxdıralım:",greeting[0])
print("Dizinin son karakterini yazdıralım:", greeting[length - 1])
 
print(greeting[2:5])        #2 karakterden başla ve 5 kadar git
print(greeting[3:])         #3'den başla ve sona kadar git
print(greeting[2:40:2])     #2 karakterden başla 40 kadar git, ikişer ikişer al

