

# NOTE FP is not known as bad per se. FP is just not used in this case, and i wanted to highlight that this code has more 
# FP principles in it

LEMON_PRICE = 10


def buy_lemons(money: float, initial_lemons, no_lemons_to_buy: int):
    # IF he has no money, don't let him buy
    if no_lemons_to_buy  * LEMON_PRICE > money:
        return 


    new_money = money - no_lemons_to_buy * LEMON_PRICE

    return (new_money, initial_lemons + no_lemons_to_buy)
    
def ask_user_for_lemons_to_buy():
    return int(input("Number of lemons to buy?"))
    
def ask_user_for_starting_cash():
    return float(input("starting money pls:\n"))

# Declare vars
age: int = None
money :float = None
no_lemons : int = 0
number_of_cups: int = 0
weight_of_ice: int = 0



money =  ask_user_for_starting_cash()


while True:
    no_lemons_to_buy = ask_user_for_lemons_to_buy()
    output = buy_lemons(money, no_lemons,no_lemons_to_buy)

    if output is not None:
        money, no_lemons = output
    else:
        print("Transaction falied")

    print(f"Money: {money}")
    print(f"No lemons {no_lemons}")











