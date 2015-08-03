import coin
import line
import hexagram

coin_one = coin.Coin()
coin_two = coin.Coin()
coin_three = coin.Coin()

def main():
    print('Welcome to the iChing.')
    print()
    print('PLACEHOLDER FOR EXPLANATION')
    print()
    user_hex = get_hexagram()
    display_hexagram(user_hex)

def get_hexagram():
    line_list = []

    for x in range(0, 6):
        toss_coins()
        return_coins()
        temp_line = get_line(coin_one, coin_two, coin_three)
        line_list.append(temp_line)       
    hex = hexagram.Hexagram(line_list[0], line_list[1], line_list[2], line_list[3], line_list[4], line_list[5])

def toss_coins():      
    input('Press enter to toss coins')
    coin_one.__flip__()
    coin_two.__flip__()
    coin_three.__flip__()

def return_coins():
    print('The results of your coin toss is: ', coin_one.__get_side_up__(), coin_two.__get_side_up__(), coin_three.__get_side_up__())

def get_line(coin_one, coin_two, coin_three):
    temp_line = line.Line(coin_one, coin_two, coin_three)
    return temp_line

def displayhexagram(example_hex):
    print('Temp')

main()
