
from appJar import gui #uncomment this for 100% submission


#Sample Team Project Extra Credit -- Shopping Application 110%
#Make sure to include the files for your team csv and .gif in your submission!
#include the app.Jar folder in the folder where your team files are stored

#Function to greet the user and ask for a category -- Vansh

import pandas
import chatbot
import tkinter #uncomment this for 100% submission
cart = ""
total = 0
bye = []
tdf=pandas.read_csv("primethreads.csv")
Jerseylist = list(tdf.Jerseys)
Hatlist = list(tdf.Hats)
Accessorieslist = list(tdf.Accessories)
def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Jerseys":
        pants("Welcome to our Jerseys section! Here are your choices:",Jerseylist,"Which Jersey would you like or enter None? ")
    elif canswer == "Hats":
        tops("Welcome to our Hats section!  Here are your choices:",Hatlist,"Which Hat would you like or enter None? ")
    elif canswer == "Accessories":
        dessert("Welcome to our Accessories section! Here are your choices:",Accessorieslist,"Which Accessory would you like or enter None? ")
    else:
        print('Sorry, we do not carry that category.  See you next time!')


#Function to ask user to pick a Jersey -- Nima
def pants(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    pantspick = input(pickq)
    if pantspick == "None":
        print("Goodbye")
    elif pantspick == "Warriors":
        closing("Warriors",40,"Enjoy your Warriors jersey!" )
    elif pantspick == "49ers":
        closing("49ers",50,"Enjoy your 49ers jersey!" )
    elif pantspick == "Giants":
        closing("Giants",100,"Enjoy your Giants jersey!" )
    elif pantspick == "Sharks":
        closing("Sharks",150,"Enjoy your Sharks jersey!" )
    else:
        closing("Earthquakes",200,"Enjoy your Earthquakes jersey!" )
    

#Function to ask user to pick a Hat -- Diego
def tops(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    toppick = input(pickq)
    if toppick == "None":
        print("Goodbye")
    elif toppick == "beanies":
        closing("beanies",10,"Enjoy your beanie!" )
    elif toppick == "caps":
        closing("caps",6,"Enjoy your cap!" )
    elif toppick == "snapbacks":
        closing("snapbacks",2,"Enjoy your snapback!" )
    elif toppick == "bucket hats":
        closing("bucket hats",8,"Enjoy your bucket hat!" )
    else:
        closing("flat caps",20,"Enjoy your flat cap!" )
        
#Function to ask user to pick an Accessory -- Jimmy
def dessert(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    toppick = input(pickq)
    if toppick == "None":
        print("Goodbye")
    elif toppick == "socks":
        closing("socks",15,"Enjoy your socks!")
    elif toppick == "flags":
        closing("flags",25,"Enjoy your flags!")
    elif toppick == "bottles":
        closing("bottles",10,"Enjoy your bottles!")
    elif toppick == "phone cases":
        closing("phone cases",16,"Enjoy your phone cases!")
    else:
        closing("lanyards",18,"Enjoy your lanyards!")
        
#Function to give user total price of purchase -- Nima
def closing(pickeditem,price,goodbye):
    global cart
    global total
    global bye
    cart = cart + " " + pickeditem
    bye.append(goodbye)
    total = total + price
    ttotal = total*1.09
    print("Your items so far:",cart)
    print("Your cost for the",pickeditem,"is $%.2f."%price)
    print("Your total cost is $%.2f."%total)
    print("Your total cost plus tax is $%.2f."%ttotal)
    more = input("Would you like to pick another item (y/n)?")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse (Jerseys, Hats, Accessories)? ", "Ready to browse (y/n)? ")
    else:
        print("Please pay $%.2f!"%ttotal)
        print("Your cart:")
        for l in cart:
            print(l,end="")
        print()
        print("Thank you for shopping with us!")
        for b in bye:
            print(b)


    
#make the code on line 119 a comment (use #) for 100% submission
        
#greet_user("Welcome to our store", "n", "What category would you like to browse (Jerseys, Hats, Acessories)? ", "Ready to browse (y/n)? ")


#Uncomment this section for 100% submission (remove the three quote marks from lines 123 and 183)
#This is the function that determines code executed when each button is pressed

#Each teammember should replace the Button name assigned to btn (see line 91 for an example) 
#in the if-elif statements below with
#a short title for his/her function.  Then place a call to the
#corresponding function on the next line

#Function allowing user to press a button to browse items or exit -- Nima

def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Hello":
        greet_user("Welcome to our store", "n", "What category would you like to browse (Jerseys, Hats, Accessories)? ", "Ready to browse (y/n)? ")
    elif btn == "Jerseys":
        pants("Welcome to our Jerseys section! Here are your choices:",Jerseylist,"Which Jersey would you like or enter None? ")
    elif btn == "Hats":
        tops("Welcome to our Hats section!  Here are your choices:",Hatlist,"Which Hat would you like or enter None? ")    
    elif btn == "Accessories":
         dessert("Welcome to our Accessories section! Here are your choices:",Accessorieslist,"Which Accessory would you like or enter None? ")
    elif btn == "Chatbot":
        chatbot.chatter()
    elif btn == "Close":
        app.infoBox("b1","Thank you for shopping!")   
    else:
        print('Pick a valid option')


#The code below defines the gui, adding buttons, labels, images, color, etc.
#
#Make changes to the title (line 163), image (line 169), and button
#names (lines 175 to 180)

#Edit 500x500 in line 159 to make your window bigger or smaller

app=gui("Main Menu","1000x800")

#Replace "Welcome to Our Store's Main Menu" with your team's greeting in line 117

app.addLabel("title", "Welcome to Prime Threads Sports Store!")
app.setLabelBg("title", "yellow")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 166

app.addImage("decor","PrimeThreads.gif")
app.setFont(30)

#change the first parameter of the addButton method in lines 172 to 177 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Hello", press)
app.addButton("Jerseys", press)
app.addButton("Hats", press)
app.addButton("Accessories", press)
app.addButton("Chatbot", press)
app.addButton("Close", press)
app.addButton("Exit",press)
app.go() #displays the gui


