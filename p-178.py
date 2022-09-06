from tkinter import *
import random

root = Tk()
root.title("Encapsulation-Random Color")
root.geometry("500x400")
root.config(bg = "white")

label_score = Label(root, text = "Score: 0",font = ("Bhlchrift Light", 15,"bold"),bg = "white")
label_score.place(relx =0.1, rely = 0.1, anchor = CENTER)
Label_name = Label(root, font = ("Ariel",40),bg = "white")
Label_name.place(relx = 0.3,rely = 0.3, anchor = CENTER)


input_value = Entry(root)
input_value.place(relx = 0.5,rely =0.5,anchor = CENTER)
class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","orange"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","pink","green","blue","yellow","orange"]
        self.random_number_for_color = random.randint(0,5)
        print(self.random_number_for_color)
        print(self.random_number_for_text)
        Label_name["text"] = self.text[self.random_number_for_text]
        Label_name["fg"] = self.color[self.random_number_for_color]
    def __update_score(self,input_value):
        if(input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0,10)
            label_score["text"] = "Score :" + str(self.__score)
    def get_user_value(self, input_value):
        self.__update_score(input_value)
obj = game()
def getInput():
    value = input_value.get()
    obj.get_user_value(value)
    obj.updateGame()
    input_value.delete(0,END)
btn1 = Button(root,text = "CHECK", command = getInput,bg = "IndianRed1", fg = "white",relief = FLAT, padx=10,pady = 1,font = ("Arial",15))
btn1.place(relx = 0.35, rely = 0.65, anchor = CENTER)

btn2 = Button(root,text = "START", command = obj.updateGame(),bg = "grey", fg = "white",relief = FLAT, padx=10,pady = 1,font = ("Arial",15))
btn2.place(relx = 0.65,rely = 0.65, anchor = CENTER)

root.mainloop()

        