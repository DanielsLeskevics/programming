class Restaurant:
    def __init__(self, name, id, address, location):
        self.name = name
        self.id= id
        self.address = address
        self.location = location
        self.menu=[]

    def add_food(self, food):
        self.menu.append(food)

class food:
    def __int__(self, type, name, price, vegetarian, glutenfree,):
        self.type = type
        self.name = name
        self.price = price
        self.glutenfree = glutenfree
        self.vegetarian = vegetarian
    
def galvena_programma():
   rest1 = Restaurant("Vairāk saules","1","Domina shopping ", (50.1234, 49.123)) 
   food1=food("Starter","Spring rolls", 4.00, True, True)
   food2=food("Salad","Cezar", 8, True, False)
   food3=food("Main","burger", 12, False, True)

    rest1.add_food(food1)
    rest1.add_food(food2)
    rest1.add_food(food3)

galvena_programma()