import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image
print("This is SS MP")

# Creating window object
window = tkinter.Tk()
window.title("Parking lot")
label = tkinter.Label(window, text="This is the parking lot")
l1 = tkinter.Label(window, text="IR Controlled Parking Lot")
window.geometry('900x700')
window.configure(bg='gray')
l1.grid(column=0, row=0)


label_entry=tkinter.Label(window, text="ENTRY", width=5, height=5)
label_entry.grid(column=7, row=3)
label_exit=tkinter.Label(window, text="EXIT", width=5, height=5)
label_exit.grid(column=7, row=8)

# Importing Images
slot_empty = Image.open('SE_1.png')
slot_empty = slot_empty.resize((100, 130), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(slot_empty)
slot_filled = Image.open('SF_1.png')
slot_filled = slot_filled.resize((100, 130), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(slot_filled)

colour="yellow" 
# Creating 5 consecutive slots
bt1 = tkinter.Button(window, text="Slot 1", image=my_img, compound='top', borderwidth=3, relief="solid")
bt1.grid(column=1, row=2)
bt2 = tkinter.Button(window, text="Slot 2", image=my_img,compound='top')
bt2.grid(column=2, row=2)
bt3 = tkinter.Button(window, text="Slot 3", image=my_img,compound='top')
bt3.grid(column=3, row=2)
bt4 = tkinter.Button(window, text="Slot 4", image=my_img,compound='top')
bt4.grid(column=4, row=2)
bt5 = tkinter.Button(window, text="Slot 5", image=my_img,compound='top')
bt5.grid(column=5, row=2)

# Creating a 3 row wide road
#l2 = tkinter.Label(window, bg="gray", text="\t")
#l2.grid(row=3)
l3 = tkinter.Label(window, bg="gray", text="Road")
l3.grid(row=3)
#l4 = tkinter.Label(window, bg="gray", text="\t")
#l4.grid(row=5)

# Creating 5 consecutive slots
bt6 = tkinter.Button(window, text="Slot 6", image=my_img,compound='top')
bt6.grid(column=1, row=6)
bt7 = tkinter.Button(window, text="Slot 7", image=my_img,compound='top')
bt7.grid(column=2, row=6)
bt8 = tkinter.Button(window, text="Slot 8", image=my_img,compound='top')
bt8.grid(column=3, row=6)
bt9 = tkinter.Button(window, text="Slot 9", image=my_img,compound='top')
bt9.grid(column=4, row=6)
bt10 = tkinter.Button(window, text="Slot 10", image=my_img,compound='top')
bt10.grid(column=5, row=6)

# Creating 5 consecutive slots
bt11 = tkinter.Button(window, text="Slot 11", image=my_img,compound='top')
bt11.grid(column=1, row=7)
bt12 = tkinter.Button(window, text="Slot 12", image=my_img,compound='top')
bt12.grid(column=2, row=7)
bt13 = tkinter.Button(window, text="Slot 13", image=my_img,compound='top')
bt13.grid(column=3, row=7)
bt14 = tkinter.Button(window, text="Slot 14", image=my_img,compound='top')
bt14.grid(column=4, row=7)
bt15 = tkinter.Button(window, text="Slot 15", image=my_img,compound='top')
bt15.grid(column=5, row=7)

# Creating a 3 row wide road
#l2 = tkinter.Label(window, bg="gray", text="\t")
#l2.grid(row=8)
l3 = tkinter.Label(window, bg="gray", text="Road")
l3.grid(row=8)
#l4 = tkinter.Label(window, bg="gray", text="\t")
#l4.grid(row=10)

# Creating 5 consecutive slots
bt16 = tkinter.Button(window, text="Slot 16", image=my_img,compound='top')
bt16.grid(column=1, row=11)
bt17 = tkinter.Button(window, text="Slot 17", image=my_img,compound='top')
bt17.grid(column=2, row=11)
bt18 = tkinter.Button(window, text="Slot 18", image=my_img,compound='top')
bt18.grid(column=3, row=11)
bt19 = tkinter.Button(window, text="Slot 19", image=my_img,compound='top')
bt19.grid(column=4, row=11)
bt20 = tkinter.Button(window, text="Slot 20", image=my_img,compound='top')
bt20.grid(column=5, row=11)



#dkt
dkt = {}
dkt[0] = (bt1)
dkt[1] = (bt2)
dkt[2] = (bt3)
dkt[3] = (bt4)
dkt[4] = (bt5)
dkt[5] = (bt6)
dkt[6] = (bt7)
dkt[7] = (bt8)
dkt[8] = (bt9)
dkt[9] = (bt10)
dkt[10] = (bt11)
dkt[11] = (bt12)
dkt[12] = (bt13)
dkt[13] = (bt14)
dkt[14] = (bt15)
dkt[15] = (bt16)
dkt[16] = (bt17)
dkt[17] = (bt18)
dkt[18] = (bt19)
dkt[19] = (bt20)

directions=["slot1 on right after entry",
"slot2 on right after entry","slot3 on right after entry","slot4 on right after entry","slot5 on right after entry",
"slot6 on left after entry","slot7 on left after entry","slot8 on left after entry","slot9 on left after entry"
,"slot10 on left after entry","slot11 on left after taking two left turns and entering into 2nd lane",
"slot12 on left after taking two left turns and entering into 2nd lane","slot13 on left after taking two left turns and entering into 2nd lane",
"slot14 on left after taking two left turns and entering into 2nd lane","slot15 on left after taking two left turns and entering into 2nd lane",
"slot16 on right after taking two left turns and entering into 2nd lane","slot17 on right after taking two left turns and entering into 2nd lane",
"slot18 on right after taking two left turns and entering into 2nd lane","slot19 on right after taking two left turns and entering into 2nd lane",
"slot20 on right after taking two left turns and entering into 2nd lane"]





def opt_1(lst):
    temp=min(lst)
    tkinter.messagebox.showinfo("Welcome to the CARPARK","{} slot is assigned to you, These are the directions :{}".format(temp+1,directions[temp]))
    dkt[temp]['image']=my_img2
    lst.remove(temp)
    
    

def opt_2(n,lst):
  tkinter.messagebox.showinfo("Welcome to the CARPARK", "{} number of cars are parked, {} slots are free".format(n,len(lst)))

  
def opt_3(slot_remove, car_slot_empty):
    dkt[slot_remove-1]['image']=my_img
    car_slot_empty.append(slot_remove-1)
    car_slot_empty.sort()

#Console Code
print("Welcome to CARPARK\n")
n = 0 #Number of Cars 
car_slot_empty=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
while (True):
    print("Enter 1 to find a parking in the CARPARK\n")
    print("Enter 2 to display status of CARPARK\n")
    print("Enter 3 to remove your car\n")
    print("Enter 4 To Exit\n")
    print("Enter Your Option:")
    x = int(input())
    if (x == 1):
        if(n<20):
            n+=1
            opt_1(car_slot_empty)
        else:
            tkinter.messagebox.showerror("Parking Allotment.",  "The garage is full, Please try later")
    elif(x == 2):
        opt_2(n,car_slot_empty)
    elif (x == 3):
        if(n>0):
          n-=1
          print("Enter the slot number of the car you want to remove:")
          slot_remove=int(input())
          if(slot_remove-1 in car_slot_empty):
              tkinter.messagebox.showinfo("Parking Allotment","Slot {} is empty".format(slot_remove))
          else:
            opt_3(slot_remove, car_slot_empty)
        else:
          tkinter.messagebox.showerror("Parking Allotment.",  "There is no car in the garage")
    elif (x == 4):
      print("Goodbye\n")
      break
    else:
      print("Enter An Valid Option")
# Main loop to keep the window open as long as user wants
window.mainloop()                                                                                                                                                                

