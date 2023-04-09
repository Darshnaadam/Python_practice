# Creating the first class and objects

class phone:
    def make_call(self):
        print("Making a phone call")

    def play_game(self):
        print("playing a game")

# Adding parameters to the class
    def assign_color(self,color):
        self.color = color

    def assign_cost(self,cost):
        self.cost = cost
    
    def show_color(self):
        print(self.color)

    def show_cost(self):
        print(self.cost)
    
    

p1 = phone()
p1.make_call()
p1.play_game()

p2 = phone()
p2.assign_color("Orange")
p2.assign_cost(50)
p2.show_color()
p2.show_cost()
