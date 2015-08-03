import coin
import line
import hexagram

coin_one = coin.Coin()
coin_two = coin.Coin()
coin_three = coin.Coin()

def main():
    print('Welcome to the iChing.')
    toss_coins()
    return_coins()
    line_one = get_line(coin_one, coin_two, coin_three)
    print(line_one.__get_type__())

def toss_coins():      
    input('Press enter to toss coins')
    coin_one.__flip__()
    coin_two.__flip__()
    coin_three.__flip__()

def return_coins():
    print(coin_one.__get_side_up__())
    print(coin_two.__get_side_up__())
    print(coin_three.__get_side_up__())

def get_line(coin_one, coin_two, coin_three):
    temp_line = line.Line(coin_one, coin_two, coin_three)
    return temp_line

main()




