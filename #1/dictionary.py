sehirler = ['Kocaeli','istanbul']
plakalar = [41,34]
result =  plakalar[sehirler.index('Kocaeli')] # Kocaelinin plaka kodunu getir

plakalar = {'kocaeli' : 41, 'istanbul' : 34}
result = plakalar['kocaeli']

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'
result = plakalar

users = {
    'sadikturan' :{
        'roles'     : ['admin', 'user'],
        'age'       : 45,
        'email'     : 'sadik@gmail.com',
        'adress'    : 'Kocaeli',
        'phone'     : '0 000 000 00 00'
    },
    'kamilklkn' :{
        'roles'     : ['admin', 'user'],
        'age'       :  28,
        'email'     : 'kamil@gmail.com',
        'adress'    : 'Erzincan',
        'phone'     : '0 000 000 00 00',
        'Web Page'  : 'www.kamilklk.com'
    }
}

result = users['sadikturan']['age']
result = users['kamilklkn']['age']
result = users['kamilklkn']['roles']


print(result)