message = 'Hello There. My name is Sadık Turan'

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize() 
# message = message.strip() 
# message = message.split('.')       #Boşluklardan itibaren disi olarak bölünür
# message = message.split()            #Boşluklardan itibaren disi olarak bölünür
# message = '*'.join(message)
# index = message.find('Sadık')
# print(index)

# isFound = message.startswith('H')
# message = print(message.strip(), "\n", isFound)

message = message.replace('Sadık','ÇINAR')
message = message.replace(' ',' * ')

message = message.center(100,'*')




print(message)

