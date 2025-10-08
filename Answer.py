from logging import root
from tkinter import *
from random import randint
from tkinter import font
from tkinter.tix import COLUMN
from tkinter import messagebox



window=Tk()                           #initialize window
window.title("Rock Paper Scissor")    #to give title to window

width=window.winfo_screenwidth()      #to get full screen window width
height=window.winfo_screenheight()    #to get full screen window height
window.geometry("%dx%d" % (width,height))

window.resizable(True,True)



####################################      username frame     ########################################

username_frame=Frame(window,width=700,height=700,bg="#fff")     #initialize frame 
username_frame.place(relx=0.5,rely=0.5,anchor=CENTER)           #give position to frame

#What do you want to be called in this game ? LABEL
username_label=Label(username_frame,text="What do you want to be called in this game ?",font=("arial",20,"bold"),bg="white",fg="black")
username_label.place(x=47,y=250)                                #give position to label

#Entrybox for name of the user
username_entrybox=Entry(username_frame,width=20,fg='black',border=2,bg='white',font=('Microsoft YaHei UI Light',20))
username_entrybox.place(x=100,y=320)
username_entrybox.focus()

#submit button for submitting username
submit_btn=Button(username_frame,text="SUBMIT",bg="#3305A3",fg="#fff",font=("arial",16,"bold"),command=lambda:get_username())
submit_btn.place(x=450,y=320)


#submit_btn - functionality of this button
def get_username():
    global username                                #declare username as global variable        
    username=username_entrybox.get().strip()       #get value from entrybox to username variable

    if(username==""):                              #user can't enter null as name
        messagebox.showwarning("Warning","Please Enter Your Name")
    elif(username.isspace()):                      #user can not enter only space as name of the user
        messagebox.showwarning("Warning","Please Enter Valid Name")
    else:
        username_frame.place_forget()

        ######## positioning the elements if user enter correct name ########

        player_indicator=Label(window,width=10,font=("arial",40,"bold"),text=username,bg="#cccccc",fg="blue")  #name of player
        computer_indicator.grid(row=0,column=1)
        player_indicator.grid(row=0,column=3)

        image_computer.grid(row=1,column=0)
        image_player.grid(row=1,column=4)

        computer_score.grid(row=1,column=1)
        player_score.grid(row=1,column=3)

        button_rock.grid(row=2,column=1)
        button_paper.grid(row=2,column=2)
        button_scissor.grid(row=2,column=3)

        final_message.place(x=485,y=130)
        new_game_btn.place(x=550,y=640)

        label_computer.place(x=60,y=275)
        label_player.place(x=1200,y=275)

        


###########################################  Rock Paper Scissor window code #########################################

#initialize images as variable
image_rock=PhotoImage(file="image1.png")       
image_paper=PhotoImage(file="image2.png")
image_scissor=PhotoImage(file="image3.png")


#name of computer
computer_indicator=Label(window,width=10,font=("arial",40,"bold"),text="COMPUTER",bg="#cccccc",fg="blue")


image_computer=Label(window,image=image_rock,width=200,height=200)         #image for computer's selected move
label_computer=Label(window,font=("arial",20,"bold"),text="Rock")          #label for computer's selected move


image_player=Label(window,image=image_scissor,width=200,height=200)        #image for player's selected move
label_player=Label(window,font=("arial",20,"bold"),text="Scissor")         #label for player's selected move


computer_score=Label(window,text=0,font=('arial',60,"bold"),fg="red")      #indicates score of computer
player_score=Label(window,text=0,font=('arial',60,"bold"),fg="red")        #indicates score of player


radio=IntVar()
################## Images as radio button to make a move for player ###########################

button_rock=Radiobutton(window,image=image_rock,command=lambda:choice_update("rock"),value=1,variable=radio)
button_paper=Radiobutton(window,image=image_paper,command=lambda:choice_update("paper"),value=2,variable=radio)
button_scissor=Radiobutton(window,image=image_scissor,command=lambda:choice_update("scissor"),value=3,variable=radio)


final_message=Label(window,font=("arial",30,"bold"),width=15,fg="#888B8D") #it indicates who won the round-player or computer or tie


another_round_label=Label(window,font=("arial",30),fg="#560319",text="Do you want another round?") #label that ask user for another round

############    yes and no buttons - to take response from user whether user wants to play another round or not  ################
yes_btn=Button(window,text="YES",width=5,height=1,relief=GROOVE,font=("arial",20,"bold"),bg="#cccccc",fg="black",command=lambda:new_round())
no_btn=Button(window,text="NO",width=5,height=1,relief=GROOVE,font=("arial",20,"bold"),bg="#cccccc",fg="black",command=lambda:no_btn_functionality())


###########  to start new game - btn  ############
new_game_btn=Button(window,text="Start New Game",width=15,height=1,relief=GROOVE,font=("arial",20,"bold"),bg="#A2BAF5",fg="black",command=lambda:new_game())





###################################################  FUNCTIONS ########################################################

#this function update the message en each round 
def msg_updation(a):              
    final_message['text']=a        #for ex. "user wins" , "it's tie" etc...


#this function updates the score of computer
def computer_update():            
    final=int(computer_score['text'])
    final+=1

    computer_score["text"]=str(final)


#this function updates the score of player
def player_update():               
    final=int(player_score['text'])
    final+=1

    player_score["text"]=str(final)


#this function checks who win round     "p-player"  "c-computer"
def winner_check(p,c):             
    if(p==c):                      #if player and computer both choose same then it's tie  
        msg_updation("It's a tie")
    elif(p=="rock"):                  
        if(c=="paper"):
            msg_updation("Computer Wins")      #if "player-rock" and "computer-paper"
            computer_update()
        else:
            msg_updation(f"{username} wins")   #if "player-rock" and "computer-scissor"
            player_update()
    elif(p=="paper"):
        if(c=="scissor"):                 
            msg_updation("Computer Wins")      #if "player-paper" and "computer-scissor"
            computer_update()
        else:
            msg_updation(f"{username} wins")   #if "player-paper" and "computer-rock"
            player_update()
    elif(p=="scissor"):
        if(c=="rock"):
            msg_updation("Computer Wins")      #if "player-scissor" and "computer-rock"
            computer_update()
        else:
            msg_updation(f"{username} wins")   #if "player-scissor" and "computer-paper"
            player_update()
    else:
        pass

to_select=["rock","paper","scissor"]        #initilizing list


#this function updates the image and label in each round according to player and computer's move
def choice_update(a):       
    choice_computer = to_select[randint(0,2)]          #computer selects randomly from ['rock','paper','scissor']
    
    if(choice_computer=="rock"):                         #if computer chosses -rock
        image_computer.configure(image=image_rock)
        label_computer['text']="Rock"
    elif(choice_computer=="paper"):                      #if computer chosses -paper
        image_computer.configure(image=image_paper)
        label_computer['text']="Paper"
    else:                                                #if computer chosses -scissor
        image_computer.configure(image=image_scissor)
        label_computer['text']="Scissor"

    
    if(a=="rock"):                                       #if player chosses -rock
        image_player.configure(image=image_rock)
        label_player['text']="Rock"
    elif(a=="paper"):                                    #if player chosses -paper
        image_player.configure(image=image_paper)
        label_player['text']="Paper"
    else:                                                #if player chosses -scissor
        image_player.configure(image=image_scissor)
        label_player['text']="Scissor"

    winner_check(a,choice_computer)

    #disable radio button after each round
    button_rock.configure(state=DISABLED)
    button_paper.configure(state=DISABLED)
    button_scissor.configure(state=DISABLED)

    #ask user for another round
    another_round_label.place(x=300,y=540) #610
    yes_btn.place(x=850,y=540)
    no_btn.place(x=990,y=540)


### functionality of YES button 
def new_round():   
    #to active radio buttons
    button_rock.configure(state=ACTIVE)
    button_paper.configure(state=ACTIVE)
    button_scissor.configure(state=ACTIVE)

    #remove unnecessory elements from window
    another_round_label.place_forget()
    yes_btn.place_forget()
    no_btn.place_forget()


### no button functionality
def no_btn_functionality():   
    #remove unnecessory elements from window
    another_round_label.place_forget()
    yes_btn.place_forget()
    no_btn.place_forget()


# new_game_btn - functionality of this button
def new_game():                  #this function sets computer score and player score to 0
    #set score to -0
    computer_score["text"]=0   
    player_score["text"]=0

    #remove unnecessory elements from window
    another_round_label.place_forget()
    yes_btn.place_forget()
    no_btn.place_forget()

    final_message["text"]="New Game"

    #to active radio buttons
    button_rock.configure(state=ACTIVE)
    button_paper.configure(state=ACTIVE)
    button_scissor.configure(state=ACTIVE)




window.mainloop()