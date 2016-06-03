import coin
import line

# Create three coin objects for use throughout program
coin_one = coin.Coin()
coin_two = coin.Coin()
coin_three = coin.Coin()

def main():
    print('Welcome to the I Ching.')
    print()
    print('You will toss six coins Each')
    print('coin toss will determine a line')
    print('of your hexagram. The program')
    print('will display your hexagram and')
    print('inform you as to which lines are')
    print('changing lines.')
    print()
    user_hex = get_hexagram() # call get_hexagram() function and assign result, a list, to user_hex
    display_hexagram(user_hex) # call display_hexagram to display user_hex

# get_hexagram() function performs all the work of obtaining a hexagram
def get_hexagram():
    line_list = [] # create empty list to put the six lines into

    for x in range(0, 6): # for loop that will toss six coins and create six line objects
        print('Press enter for coin toss number', (x+1))
        input()
        toss_coins() # call toss_coins() func
        return_coins() #call return_coins() func
        temp_line = get_line(coin_one, coin_two, coin_three)
        line_list.append(temp_line)       
    return line_list

def toss_coins(): # toss the coins
    coin_one.__flip__()
    coin_two.__flip__()
    coin_three.__flip__()

def return_coins(): # return current value of coins
    print('The results of your coin toss is: ', coin_one.__get_side_up__(), coin_two.__get_side_up__(), coin_three.__get_side_up__())
    print()
    
def get_line(coin_one, coin_two, coin_three):
    temp_line = line.Line(coin_one, coin_two, coin_three)
    return temp_line

def display_hexagram(line_list):
    print('Your Hexagram is:')
    print()
    for x in range(5, -1, -1):
        if line_list[x].type == 'Broken':
            print('Line', (x+1), '---  ---')
        else:
            print('Line', (x+1), '--------')
    print()
    for x in range(0, 6):
        if line_list[x].changing == True:
            print('Line', (x+1), 'is a changing line.')

main()
