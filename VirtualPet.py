class VirtualPet:
    """An implementation of a virtual pet"""
    def talk(self):
        print("Hello, I am your new pet and i have been called {0}".format(self.name))
        if self.hunger<50:
            print("please feed me, I'm hungry")

        

            
        
    def __init__(self,name):
        self.name=name
        self.hunger=50

    def OptionMenu ():
        print("*****WHAT WOULD YOU LIKE TO DO WITH YOUR PET*****")
        print()
        print("1.feed")
        print("2.walk")
        

    def OptionChoice(

    def eat (self,hunger,food):
        if food == "cookie":
            self.hunger=self.hunger-8
            print("my hunger is now {0}/100".fomat(self.hunger))
        elif food == "raisin":
            self.hunger=self.hunger-2
            print("my hunger is now {0}/100".fomat(self.hunger))
        elif food == "burger":
            self.hunger=self.hunger-40
            print("my hunger is now {0}/100".fomat(self.hunger))
        elif food == "rib":
            self.hunger=self.hunger-30
            print("my hunger is now {0}/100".fomat(self.hunger))
        elif food == "apple":
            self.hunger=self.hunger-10
            print("my hunger is now {0}/100".fomat(self.hunger))
        elif food == "sausage":
            self.hunger=self.hunger-25
            print("my hunger is now {0}/100".fomat(self.hunger))
        else:
            print("unfortunately, your pet can't eat that, please choose something from the menu")
        if self.hunger==100:
            print("I am too full, I can't eat anymore")
        print("that {0} was tasty".format(food))

            
        def walk(self,places):
            
            
if __name__=="__main__":
    name=input("What do you want to call your pet: ")
    pet_one=VirtualPet(name)
    pet_one.talk()
    food=input("what would you like to eat (cookie, raisin, burger, rib, apple,sausage): ")
    pet_one.eat(food)
    places=input("where would you like to walk(park,petshop,the depths of hell): ") 
    pet_one.walk(places)
    
    
