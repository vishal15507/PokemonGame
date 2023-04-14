from turtle import Turtle,register_shape

list=['axew','gible','taillow','charizard','Mega_Charizard_X','Mega_Charizard_Y','pikachu','electabuzz','hitmonchan','carracosta','torterra','machoke','drapion','gengar','Mega_Gengar','grimmsnarl','golem','floatzel','Mega_Blastoise']
path_pokemon="/Users/HP/PycharmProjects/pong_game/pokemons/"

class Pokemon_start(Turtle):
    def __init__(self):
        super().__init__()
        self.constant=0
        #self.my_shoot=[]
        for i in range(len(list)):
            register_shape(f"{path_pokemon}{list[i]}.gif")
            register_shape(f"{path_pokemon}{list[i]}_right.gif")
            #self.my_shoot.append(f"{list[i]}_attack.gif")
        self.shape("/Users/HP/PycharmProjects/pong_game/pokemons/charizard.gif")
        self.penup()
        # self.go_back=True


    def left(self):
        # tim.shape("charizard.gif")
        current_shape = self.shape()
        for i in range(len(list)):
            if current_shape == f"{path_pokemon}{list[i]}.gif" or current_shape == f"{path_pokemon}{list[i]}_right.gif":
                self.shape(f"{path_pokemon}{list[i]}.gif")
        self.setheading(180)
        self.forward(20)

    def right(self):
        current_shape = self.shape()
        for i in range(len(list)):
            if current_shape == f"{path_pokemon}{list[i]}.gif" or current_shape == f"{path_pokemon}{list[i]}_right.gif":
                self.shape(f"{path_pokemon}{list[i]}_right.gif")
        self.setheading(0)
        self.forward(20)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)

    def change_pokemon(self):
        current_shape = self.shape()
        #print(current_shape)
        for i in range(len(list)):

            if current_shape == f"{path_pokemon}{list[i]}.gif":
                print(list[i])
                if i == (len(list) - 1):
                    self.shape(f"{path_pokemon}{list[0]}.gif")

                else:
                    self.shape(f"{path_pokemon}{list[i + 1]}.gif")
            elif current_shape == f"{path_pokemon}{list[i]}_right.gif":
                if i == (len(list) - 1):
                    self.shape(f"{path_pokemon}{list[0]}_right.gif")
                else:
                    self.shape(f"{path_pokemon}{list[i + 1]}_right.gif")
            else:
                pass
            # tim.shape(f"{list[count]}.gif")
            # print(f"abc{count}")
            # change_pokemon()
    def pokemon_count(self):
        if self.constant+1<len(list):
            self.constant=self.constant+1
        else:
            self.constant=0
        print(list[self.constant])
    def pokemon_back(self):
        if self.constant==0:
            self.constant=len(list)-1
        else:
            self.constant=self.constant-1
        print(list[self.constant])
    def choose_pokemon(self):
        current_shape = self.shape()
        for i in range(len(list)):

            if current_shape == f"{path_pokemon}{list[i]}.gif":
                    self.shape(f"{path_pokemon}{list[self.constant]}.gif")
            elif current_shape == f"{path_pokemon}{list[i]}_right.gif":
                    self.shape(f"{path_pokemon}{list[self.constant]}_right.gif")
            else:
                pass


    def turn(self):
        self.left(90)

    # def pokemon_back(self):
    #     self.go_back=True



#if want to track the number of loops in main function from another file
#make a num variable in main file and keep increasing its value wrt loop
#and make a getnum(num) in the another file and take num as arg and this
#function keep track the number of loop thats been going on from another
#file so if want use this nth number with condition u can use it by making
#it equal to a variable fun_num in the another file;