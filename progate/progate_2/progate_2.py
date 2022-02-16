fruits = ['apple', 'banana', 'orange']

print(fruits[0])

print('好きな果物は' + fruits[2] + 'です')

fruits.append('grape')

print(fruits)

fruits[0] = 'cherry'

print(fruits[0])

for fruit in fruits:
    print(fruit)

foods = {'sushi' : 'Japan', 'curry': 'India', 'pho': 'Vietnam'}
print('sushiの発祥は' + foods['sushi'] + 'です')

for food_key in foods:
    print(food_key + 'の発祥は' + foods[food_key] + 'です')

x = 5
while x >= 0:
    print(x)
    x -= 1

numbers = [555, 666, 777, 888]

for number in numbers:
    print(number)
    if number == 777:
        print('Found!!')
        break

for number2 in numbers:
    if number2 % 2 == 0:
        continue
    print(number2)


items = {'apple':100, 'banana':200, 'orange':400}

for item_name in items:
    print('---------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input('購入する' + item_name +'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    count = int(input_count)
    total_price = items[item_name] * count

    print('支払い金額は' + str(total_price) + '円です')

    
