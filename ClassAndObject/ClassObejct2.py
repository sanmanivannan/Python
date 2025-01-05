class Human():
    def __init__(self,name,occupation):   #first have the initlization function/method to enter the parameters
        self.name = name               # then set the properties you wanted....
        self.occupation = occupation

    def do_occupation(self):        # function/method 1     
        if self.occupation == "Actor":
            print(self.name,"is an Actor")
        elif self.occupation == "Player":
            print(self.name,"is a player")

    def speaks(self):               # function/method 2
        print(self.name, "speaks English")       


Person1 = Human("Tom","Actor") #creating new object called "Person1" from class "Human" which is created above
Person1.do_occupation()
Person1.speaks()