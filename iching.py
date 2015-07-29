import coin

coin_one = coin.Coin()
coin_two = coin.Coin()
coin_three = coin.Coin()

def main():
    intro_screen()

def intro_screen():
    print('Welcome to the iChing.')
    input('Press enter to toss coins')
    toss_coins()
    return_coins()

def toss_coins():      
    coin_one.__flip__()
    coin_two.__flip__()
    coin_three.__flip__()


def return_coins():
    print(coin_one.__get_side_up__())
    print(coin_two.__get_side_up__())
    print(coin_three.__get_side_up__())


main()



