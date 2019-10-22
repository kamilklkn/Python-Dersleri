# Müşteri bilgileri tanımlama


customerName        = 'Hasan'
customerSurname     = 'Yalçın'
customerNameSurname =  customerName +' '+ customerSurname
customerGender      = 'Erke'
customerTCno        = '00000000000'
customerYarOfBirt   = 1991
customerAdress      = "Sancaktepe/ISTANBUL"
customerAge         = 2019 - customerYarOfBirt

print(customerAge)

"""
    Aşağıdaki siparişlerin toplam bilgisini hesaplayın
    Sipariş 1 => 110 Tl
    Sipariş 2 => 1100.5 Tl
    Sipariş 3 => 356.95 Tl
"""

order_1 = 110
order_2 = 1100.5
order_3 = 356.95

total = order_1 + order_2 + order_3

print("Toplam:", total)