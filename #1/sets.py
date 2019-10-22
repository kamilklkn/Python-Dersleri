fruits = {'orange', 'apple','banana'}


for x in fruits:
    print(x)
    print('*'*30)

fruits.add('cherry')
fruits.update('mango', 'grape','apple')

fruits.remove('mango')

print(fruits)
  