from tkinter import *
import meter

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Virtual Plant")
        
        cactus = "          \n"
        cactus += "       *-*,\n"
        cactus += "    ,*\/|`| \ \n"
        cactus += "      \'   |'**, -\n"
        cactus += "        \ `| | |/ ) \n"
        cactus += "        | |'| , / \n"
        cactus += "       |'| |, / \n"
        cactus += "      __|_|_|_|__ \n"
        cactus += "      [___________] \n"
        cactus += "      |          | \n"
        cactus += "      |          | \n"
        cactus += "      |          | \n"
        cactus += "      |__________| \n"
        cactus += "       |________|  \n"


        self.label = Label(master, text=cactus, font=("Courier", 20))
        self.label.pack()

        #create a function that creates functions that check each gauge
        self.example = Label(master, text="Hi there! Press enter to talk to me.")
        self.example.pack()

        self.water_meter = meter.Meter("Water")
        self.fert_meter = meter.Meter("Fertilizer")
        self.sun_meter = meter.Meter("Sunlight")
        self.love_meter = meter.Meter("Love")


        self.i = 0
        self.user = "USER"
        self.plant = "PLANT"

    def catchUserName(self, event):
        self.user = self.enterName.get()

    def userName(self):
        self.enterName = Entry(root)
        self.enterName.pack()
        self.enterName.bind('<Return>', self.catchUserName)
    
    def userintro(self, event):
        if (self.i < 4):
            self.example.config(text=userintro[self.i])
            self.i += 1
        elif (self.i == 4):
            self.userName()
            self.i += 1
        elif (self.i == 5):
            if (self.user == "USER"): 
                self.catchName(event)
            else:
                self.example.config(text="Your name is... " + self.user + "?")
                self.enterName.pack_forget()
                self.i = 0
                root.bind('<Return>', my_gui.plantintro)
            
    def catchPlantName(self, event):
        self.plant = self.enterName.get()

    def plantName(self):
        self.enterName = Entry(root)
        self.enterName.pack()
        self.enterName.bind('<Return>', self.catchPlantName)
        
    def plantintro(self, event):
        if (self.i < 5):
            self.example.config(text=plantintro[self.i])
            self.i += 1
        elif (self.i == 5):
            self.plantName()
            self.i += 1
        elif (self.i == 6):
            if (self.plant == "PLANT"): 
                self.catchPlantName(event)
            else:
                self.example.config(text="Woah... " + self.plant + "?")
                self.enterName.pack_forget()
                self.i += 1
        elif (self.i < 10):
            self.example.config(text=plantintro[self.i])
            self.i += 1
        elif (self.i == 10):
            self.example.config(text=plantintro[self.i] + self.user +".")
            self.i += 1
        elif (self.i == 11):
            self.example.config(text=plantintro[self.i])
            self.i = 0
            root.bind('<Return>', my_gui.tutorial)

    def water(self):
        self.example.config(text="How refreshing! Thanks for the drink.")
        self.water_meter.add()
        self.meterpicw.config(text=self.water_meter.print())
        self.meterpicw.place(x=15,y=30)
    def fert(self):
        self.example.config(text="Woohoo! What a boost for the day!")
        self.fert_meter.add()
        self.meterpicf.config(text=self.fert_meter.print())
        self.meterpicf.place(x=15,y=50)
    def sunlight(self):
        self.example.config(text="Time to get some melanin. #plantgirlmagic")
        self.sun_meter.add()
        self.meterpics.config(text=self.sun_meter.print())
        self.meterpics.place(x=15,y=70)
    def luv(self):
        self.example.config(text="I love you too, " + self.user + "!")
        self.love_meter.add()
        self.meterpicl.config(text=self.love_meter.print())
        self.meterpicl.place(x=15,y=90)

    def tutorial(self, event):
        if (self.i < 3):
            self.example.config(text=tutorial[self.i])
            self.i += 1
        elif (self.i == 3):
            buttons = Frame(root)
            buttons.pack()
            
            self.meterpicw = Label(root, text=self.water_meter.print(), font=("Courier", 15))
            self.water = Button(buttons, text="Water", command=self.water)
            self.water.pack(side=LEFT)

            self.meterpicf = Label(root, text=self.fert_meter.print(), font=("Courier", 15))
            self.fertilize = Button(buttons, text="Fertilize", command=self.fert)
            self.fertilize.pack(side=LEFT)

            self.meterpics = Label(root, text=self.sun_meter.print(), font=("Courier", 15))
            self.sun = Button(buttons, text="Take to Window", command=self.sunlight)
            self.sun.pack(side=LEFT)
            
            self.meterpicl = Label(root, text=self.love_meter.print(), font=("Courier", 15))
            self.love = Button(buttons, text="Love", command=self.luv)
            self.love.pack(side=LEFT)
            
            self.i += 1
        elif (self.i < 9):
            self.example.config(text=tutorial[self.i])
            self.i += 1
        elif (self.i == 9):
            self.water_meter.deplete()
            self.water_meter.deplete()
            self.sun_meter.deplete()
            self.love_meter.deplete()
            self.love_meter.deplete()
            self.meterpicw.config(text=self.water_meter.print())
            self.meterpics.config(text=self.sun_meter.print())
            self.meterpicl.config(text=self.love_meter.print())
            self.i += 1
            self.example.config(text="Well, would you look at that? Do what you gotta do! \n Press enter when you are finished.")
        elif (self.i == 10):
            if (self.water_meter.checkMeter() == 5 & self.sun_meter.checkMeter() == 5 & self.love_meter.checkMeter() == 5):
                self.i += 1
                self.example.config(text="My meters will start to go down now. \n Keep me alive, " + self.user + "!")
                self.update_water()
            else:
               self.example.config(text="Fill all of my meters, please!") 
                
    def gameover(self, event):
        self.example.config(text=self.plant + " has died.")

    def disable(self):
        self.water.config(state=DISABLED)
        self.love.config(state=DISABLED)
        self.sun.config(state=DISABLED)
        self.fertilize.config(state=DISABLED)

    def update_water(self):
        global each, limit, period
        if (each <= limit):
            each += 1
            root.after(period*1000, self.update_water)
        else:
            if (self.water_meter.checkMeter() > 1):
                self.water_meter.deplete()
                self.meterpicw.config(text=self.water_meter.print())
                self.update_love()
            else:
                self.water_meter.deplete()
                self.meterpicw.config(text=self.water_meter.print())
                self.example.config(text="My leaves are drying up, " + self.user + "... \n Press enter.")
                self.disable()
                root.bind('<Return>', my_gui.gameover)
            
    def update_love(self):
        global each, limit, period
        if (each >= limit):
            each -= 1
            root.after(period*100, self.update_love)
        else:
            if (self.love_meter.checkMeter() > 1):
                self.love_meter.deplete()
                self.meterpicl.config(text=self.love_meter.print())
                self.update_sun()
            else:
                self.love_meter.deplete()
                self.meterpicl.config(text=self.love_meter.print())
                self.example.config(text="I don't feel so good... " + self.user + "? \n Press enter.")
                self.disable()
                root.bind('<Return>', my_gui.gameover)
            
    def update_sun(self):
        global each, limit, period
        if (each <= limit):
            each += 1
            root.after(period*10, self.update_sun)
        else:
            if (self.sun_meter.checkMeter() > 1):
                self.sun_meter.deplete()
                self.meterpics.config(text=self.sun_meter.print())
                self.update_fert()
            else:
                self.sun_meter.deplete()
                self.meterpics.config(text=self.sun_meter.print())
                self.example.config(text="I'm turning brown... \n Press enter.")
                self.disable()
                root.bind('<Return>', my_gui.gameover)
            
    def update_fert(self):
        global each, limit, period
        if (each >= limit):
            each -= 1
            root.after(period*1000, self.update_fert)
        else:
            if (self.fert_meter.checkMeter() > 1):
                self.fert_meter.deplete()
                self.meterpicf.config(text=self.fert_meter.print())
                self.update_water()
            else:
                self.fert_meter.deplete()
                self.meterpicf.config(text=self.fert_meter.print())
                self.example.config(text="Why do I feel so dizzy? \n Press enter.")
                self.disable()
                root.bind('<Return>', my_gui.gameover)
    
root = Tk()
root.geometry("440x400")
my_gui = MyFirstGUI(root)

limit = 3
period = 2
each = 0

root.bind('<Return>', my_gui.userintro)
                          
userintro = ["I am a virtual plant!", "Virtual plants are a lot like real plants.",
            "We need water, sunlight, fertilizer, and lots of love.","What's your name?"]
plantintro = ["That's a cool name.", "I don't know my name.", "I know I am a cactus and that I like water.",
            "Do you want to name me?", "What do you think my name should be?","","","It's perfect!",
            "I can't think of a better name.", "I can't believe I get to have a plant parent.",
            "I already love you, ", "Sorry... too soon?"]
tutorial = ["Anyways, I should probably teach you how to keep me alive.", "Like I've said before, I need water, sunlight, fertilizer, and love.",
            "Just click on any of those buttons below me.", "", "Not so hard, right?", "Hopefully I won't be too much of a burden.",
            "On the left side of the screen, you can see my meters.", "If I don't get enough, then I'll get really sick.",
            "Then I won't be able to see your beautiful face!"]

root.mainloop()
