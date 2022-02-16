import utils
# random モジュールを読み込んでください
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if utils.validate(player_hand):
    # randint を用いて 0 から 2 までの数値を取得し、変数 computer_hand に代入してください
    computer_hand = random.randint(0,2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'コンピューター')
    
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
