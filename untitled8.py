from tkinter import *
import random

root = Tk()

root.title("Picnic Bag")
root.geometry("500x500")
label = Label(root)
label2 = Label(root)

list1 = ["BOTTLE", "LUNCH", "GAMES", "CAP", "HANKEY","SUNGLASSES"]
print(list1)
label["text"] = "Listed Items" + str(list1)


def random_number():
    random_no = random.randint(0,4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("First Item to put in is :- " + random_lucky_friend)
    
    label2["text"] = "Keep " + str(random_lucky_friend) + " in the bag"


    
btn1 = Button(root)
btn1 = Button(root, text="Which I tem to put in the bag?  ", command = random_number)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()