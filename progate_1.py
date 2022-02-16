name = "John"

print(name)

age = 24

print("私は" + str(age) + "さいです")

money = 500
apple_price = 120

if money > apple_price:
    print('リンゴを買うことができます')
else:
    print('sorry')

score = 90

if score > 90:
    print('good')
elif score == 90:
    print('soso')
else:
    print('bad')

x = 20

if 10 < x < 30:
    print("20kurai")

y = 77

if not y == 100:
    print("満点を目指せ")

grape_price = 200

input_count = input('何個買うん')

count = int(input_count)
total_price = grape_price * count

print("合計は" + str(total_price) + "こです")