class Line:
    def __init__(self, coin_one, coin_two, coin_three)

        if coin_one.side_up == 'Heads':
            coin_one_val = 3
        else:
            coin_one_val = 2

        if coin_two.side_up == 'Heads':
            coin_two_val = 3
        else:
            coin_two_val = 2

        if coin_three.side_up == 'Heads':
            coin_three_val = 3
        else:
            coin_three_val = 2

        total_coin_val = coin_one_val + coin_two_val + coin_three_val
        
        if total_coin_val % 2 == 0:
            self.type = 'Broken'
        else
            self.type = 'Solid'

        if total_coin_val == 6 or total_coin_val == 9:
            self.changing = True
        else
            self.changing = False


    def __get_type__(self):
        return self.type

    def __get_changing__(self):
        return self.changing
