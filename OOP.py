
LEMON_PRICE = 10


# This is an error handling class for easier debugging when the code base gets very big (I don't do this in my own code but it's a good habit)
class InsufficientFundsError(Exception):
    """Exception raised when there is not enough money to complete a purchase."""
    pass



class Person:
    # The name parameter here allows declaration of a variable called name
    def __init__(self,name: str, money: float):
        

        # The colons ":" are typehints. They are not essential, but provide a clearer programming experience
        self.name = name
        self.money: float = money
        self.no_lemons : int = 0
    

    

    def buy_lemons(self, no_lemons_to_buy: int) -> None:
        """Allows a user to buy lemons. An error is raised if not enough money is present

        :param no_lemons_to_buy: Number of lemons the user wants to buy
        :type no_lemons_to_buy: int
        """
        
        # we are going to try to convert this into an integer. If it fails, we raise an error as we expected an integer
        # Sometimes, you would want to raise an error even if the object is not convertable. 
        # These situations are nuanced. For now, we'll just attempt to convert it

        try:
            no_lemons_to_buy = int(no_lemons_to_buy)
        except ValueError:
            # You want to try to make your error messages as clear as possible. Try imporving on this one
            raise ValueError(f"Unable to convert {no_lemons_to_buy} to int.") 

        if no_lemons_to_buy  * LEMON_PRICE > self.money:
            # The string formating used here is f strings.
            raise InsufficientFundsError(f"{self.name} only has ${self.money},which not enough to buy {no_lemons_to_buy} for ${LEMON_PRICE} each, totalling ${LEMON_PRICE * no_lemons_to_buy}") 


        self.money = self.money - no_lemons_to_buy * LEMON_PRICE
        self.no_lemons  = self.no_lemons + no_lemons_to_buy # You can search up the += operator

     
# This is just for showcasing. 
starting_money =  float(input("How much money should haoqin start with?\n"))


# Here is the integration of classes
haoqin = Person("Haoqin", starting_money)

# these are f-strings. They are a way of formatting strings
print(f"Current user: {haoqin.name}")

while True:

    lemons_to_buy = input(f"How many lemons does {haoqin.name} want to buy?\n")

    haoqin.buy_lemons(lemons_to_buy)

    print(f"{haoqin.name} has ${haoqin.money} left, and {haoqin.no_lemons} lemons")






        