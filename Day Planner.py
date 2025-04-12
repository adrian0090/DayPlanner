import tkinter.messagebox
from calendar import Month
from os import write, remove
from tkinter import *
import time
from datetime import datetime
from geopy.geocoders import Nominatim
import requests
from tkinter import messagebox
from tkinter import ttk
import schedule


from pycparser.c_ast import While


def weather():

    """this function is for getting weather"""
    try:
        global city_weather
        global temp_label

        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city_weather.get())
        lat = location.latitude
        lng = location.longitude

        api_key = "93a58e525379a2740a14faa32add98f1"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)


        temp_label.config(text=f"\n{temp}\n{condition}\n{description}")

    except AttributeError:

        temp_label.config(text="enter city!")

def note(user_note):
    with open("your_notes.txt", "a") as write:
        write.write(f"{(str(datetime.today()).split(' '))[0]}: {user_note}\n")
        print("dastor anjam shod")


def sign_in():
    global ename
    login = Toplevel()
    ename = Entry(login, font=("Arial", 30))
    ename.grid(row=0, column=1, pady=10)
    lname = Label(login,text="name: ", font=("Arial", 30))
    lname.grid(row=0, column=0, pady=10)

    def error(user_name, user_fam, user_age, user_blood):
        x = 0
        if user_name.get().strip() == "":
            messagebox.showerror("error", "enter name!")
            x += 1
        if user_fam.get().strip() == "":
            messagebox.showerror("error", "enter last name!")
            x += 1
        if user_age.get().strip() == "":
            messagebox.showerror("error", "enter your age!")
            x += 1
        if len(user_blood.get()) > 5:
            messagebox.showerror("error", "enter one blood type!")
            x += 1

        return x



    elastname = Entry(login, font=("Arial", 30))
    elastname.grid(row=1, column=1, pady=10)
    llastname = Label(login,text="last name: ", font=("Arial", 30))
    llastname.grid(row=1, column=0, pady=10)

    age = Entry(login, font=("Arial", 30))
    age.grid(row=2, column=1, pady=10)
    lage = Label(login, text="Age: ", font=("Arial", 30))
    lage.grid(row=2, column=0, pady=10)


    Label(login, text="Blood Type:", font=("Arial", 30)).grid(row=5)

    Str_ = StringVar()

    Radiobutton(login, text="A+", variable=Str_, value="A+").grid(row=6)

    Radiobutton(login, text="A-", variable=Str_, value="A-").grid(row=7)

    Radiobutton(login, text="B+", variable=Str_, value="B+").grid(row=8)

    Radiobutton(login, text="B-", variable=Str_, value="B-").grid(row=9)

    Radiobutton(login, text="AB+", variable=Str_, value="AB+").grid(row=10)

    Radiobutton(login, text="AB-", variable=Str_, value="AB-").grid(row=11)

    Radiobutton(login, text="o+", variable=Str_, value="o+").grid(row=12)

    Radiobutton(login, text="o-", variable=Str_, value="o-").grid(row=13)


    def link():

        if error(ename, elastname, age, Str_) > 0:
            destoy()
        else:
            write1()
            destoy()
            # deslable()
            show()

    def write1():
        global BlType
        BlType = Str_.get()
        try:
            with open("data.txt", "w") as data:
                data.write(f"{ename.get()},{elastname.get()},{age.get()},{Str_.get()}")

        except Exception:
            pass

    def destoy():
        login.destroy()

    def deslable():
        signin_btn.destroy()

    btcheck = Button(login, text="Check!", font=("Arial", 30), fg="WHITE", bg="CYAN", command=link)
    btcheck.grid(row=4, column=1)


def clean(parent, btn1, btn2, btn3, btn4, line1, line2, line3, line4):
    for item in parent.winfo_children():
        if item not in [btn1, btn2, btn3, btn4, line1, line2, line3, line4]:
            item.destroy()


def time_():

    Time = Toplevel()

    check = True

    x = 0

    show_time_now = Label(Time, font=("Arial", 30, "bold"))
    show_time_now.grid(row=0, column=1)
#-------------مطالعه------------

    def time_now():
        now = datetime.now().strftime("%H:%M:%S")
        show_time_now.config(text=now)
        show_time_now.after(1000, time_now)
    time_now()

#-------------------------------
    showL = Label(Time, text="", font=("Arial", 30, "bold"))
    showL.grid(row=2, column=1)

    # تابع شروع شمارش
    def start():
        global counter
        counter = 0  # مقداردهی اولیه به شمارنده
        update_timer()  # شروع شمارش

    # تابع برای متوقف کردن شمارش
    def stop():
        global counter
        counter = -1  # متوقف کردن شمارش

    # تابع به‌روزرسانی شمارش
    def update_timer():
        global counter
        if counter != -1:  # اگر شمارش‌گر متوقف نشده باشد
            counter += 1
            showL.config(text=str(counter))  # به‌روزرسانی متن برچسب
            showL.after(1000, update_timer)

    cornometr = Button(Time, text="Stopwatch", font=("Arial", 30, "bold"), command=start)
    cornometr.grid(row=1, column=1, padx=100, pady=100)




    stop = Button(Time, text="Stop", font=("Arial", 30, "bold"), command=stop)
    stop.grid(row=3, column=1)



    Time.mainloop()


def today():
    Today = (str(datetime.today()).split(" "))[0]

    Year = Today.split("-")[0]

    Month = Today.split("-")[1]
    if Month == "01":
        Month = "January"

    elif Month == "02":
        Month = "February"

    elif Month == "03":
        Month = "March"

    elif Month == "04":
        Month = "April"

    elif Month == "05":
        Month = "May"

    elif Month == "06":
        Month = "June"

    elif Month == "07":
        Month = "July"

    elif Month == "08":
        Month = "August"

    elif Month == "09":
        Month = "September"

    elif Month == "10":
        Month = "October"

    elif Month == "11":
        Month = "November"

    elif Month == "12":
        Month = "December"


    Day = Today.split("-")[2]


    return f"{Year} {Month} {Day}"


def health():
    salamat = Toplevel()

    Blo_Type = info_label3.cget("text")
    Blo_Type = Blo_Type.split(" ")
    Blo_Type = Blo_Type[2]
    Blo_Type.strip()
    Label(salamat, text=Blo_Type).grid(row=0)
    Bl_good = (Label(salamat, text="", fg="GREEN", font=("Arial", 40, "bold")))
    Bl_good.grid(row=1)
    Bl_Bad = (Label(salamat, text="", fg="RED", font=("Arial", 40, "bold")))
    Bl_Bad.grid(row=2)
    Bl_info = Label(salamat, text="", fg="BLUE", font=("Arial", 40, "bold"))
    Bl_info.grid(row=3)

    if Blo_Type in ["O+", "O-"]:
        Bl_good.config(text=f"good food for {Blo_Type}:\nAnimal proteins like red meat\negg\nfish"
                            f"\nfruit\nvegetables")

        Bl_Bad.config(text=f"Bad foods for {Blo_Type}:\nDairy, cereals and legumes")

        Bl_info.config(text=f"{Blo_Type}-This group pays more attention to high-protein diets")

    if Blo_Type in ["A+", "A-"]:
        Bl_good.config(text=f"good food for {Blo_Type}\nvegetables\nfruits\nbeans\nnuts")

        Bl_Bad.config(text=f"Bad for {Blo_Type}\nred meat\nHeavy Dairy")

        Bl_info.config(text=f"{Blo_Type}-This group may benefit better from lighter foods")

    if Blo_Type in ["B+", "B-"]:
        Bl_good.config(text=f"good food for {Blo_Type}\nDiary\nred meat\negg\nfruit")

        Bl_Bad.config(text=f"Bad for {Blo_Type}\nchicken\nwheat\ntomato")

        Bl_info.config(text=f"{Blo_Type}-This group can benefit from different foods")

    if Blo_Type in ["AB+", "AB-"]:
        Bl_good.config(text=f"good food for {Blo_Type}\nLight foods\nfish\ndiary\nvegetables")

        Bl_Bad.config(text=f"Bad for {Blo_Type}\nred meat\nProcessed food")

        Bl_info.config(text=f"{Blo_Type}-This group may be better off eating lighter\n foods and eating a variety of foods")


    salamat.mainloop()
def Planner():
    Planner_root = Toplevel()
    global STR
    STR = StringVar()

    def read_task(user_write: "y"):
        row_counter = 0
        with open("Planner.txt", "r") as read:
            add_task(user_write)
            data = read.read()
            data = data.split(",")
            data = data[:-1]

            def hover(button):
                button.config(bg="GRAY")

            # ایجاد دکمه‌ها با استفاده از حلقه `for`
            row_counter = 0
            for i in data:
                if i == "y":
                    continue

                def create_button_command():
                    btn_master.config(bg="GRAY")


                btn_master = Button(Planner_root, text=i, bg="WHITE", fg="BLACK", command=create_button_command)
                btn_master.grid(row=row_counter)
                row_counter += 1

    add_task_ = Entry(Planner_root, font=("Arial", 30, "bold"))
    add_task_.grid(row=5, column=0)
    def link():

        x = add_task_.get()
        read_task(str(x))

    add_task_btn = Button(Planner_root, text="Add", fg="Blue", bg="CYAN", command=link)
    add_task_btn.grid(row=6, column=0)
    def add_task(user_task):
        with open("Planner.txt", "a") as write:
            write.write(f"{user_task},")

def notes():

    notess = Toplevel()

    def clear():
        with open("your_notes.txt", "w") as write:
            write.write("")

    def send():
        global ename
        final_send = f"{datetime.now()}: \n {enter.get()} \n dear"

        with open("your_notes.txt", "r") as read:
            showl.config(text=read.read())

        with open("your_notes.txt", "a") as write:
            write.write(final_send)

    showl = Label(notess, text="", font=("Arial", 30))
    showl.grid(row=0)

    enter = Entry(notess, font=("Arial", 30))
    enter.grid(row=1)

    btn_send = Button(notess, text="send", command=send, font=("Arial", 30))
    btn_send.grid(row=2)

    btn_show = Button(notess, text="show", command=send, font=("Arial", 30))
    btn_show.grid(row=3)

    btn_clear = Button(notess, text="Clear!", command=clear, font=("Arial", 30))
    btn_clear.grid(row=4)



    notess.mainloop()









def show():
    global info_label
    with open("data.txt", "r") as read:
        content = read.read()
        content = content.split(",")

        info_label.config(text=f"Name: {content[0]}")
        info_label1.config(text=f"family Name: {content[1]}")
        info_label2.config(text=f"Age: {content[2]}")
        info_label3.config(text=f"Blood type: {content[3]}")
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_week = week_days[datetime.now().weekday()]

root = Tk()

root.geometry('1200x625+100+100')

root.title("day planner")

root.resizable(0, 0)

#=========================================

btn_Time = Button(root, text="Time", font=("Arial", 30, "bold"), width=13, height=2, bg="#00879E",
                     fg="WHITE", bd=0, command=time_)
btn_Time.grid(row=1, column=0, pady=10, padx= 10)


btn_Planner = Button(root, text="Planner", font=("Arial", 30, "bold"), width=13, height=2, bg="#00879E",
                     fg="WHITE", bd=0, command=Planner)
btn_Planner.grid(row=2, column=0, pady=10, padx= 10)


btn_Notes = Button(root, text="Notes", font=("Arial", 30, "bold"), width=13, height=2, bg="#00879E",
                     fg="WHITE", bd=0, command=notes)
btn_Notes.grid(row=3, column=0, pady=10, padx= 10)


btn_Health = Button(root, text="Health", font=("Arial", 30, "bold"), width=13, height=2, bg="#00879E",
                     fg="WHITE", bd=0, command=health)
btn_Health.grid(row=4, column=0, pady=10, padx= 10)

#=========================================

line_1 = Label(root, text="", height=10, bg="#66D2CE")
line_1.grid(row=1, column=1, padx=40)


line_2 = Label(root, text="", height=10, bg="#66D2CE")
line_2.grid(row=2, column=1, padx=40)


line_3 = Label(root, text="", height=10, bg="#66D2CE")
line_3.grid(row=3, column=1, padx=40)


line_4 = Label(root, text="", height=10, bg="#66D2CE")
line_4.grid(row=4, column=1, padx=40)

back_week = Label(root, text="", width=105,height=8, bg="#624E88")
back_week.place(x=415, y=15)

Monday = Label(root, text="  Monday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Monday.grid(row=1, column=2)


Tuesday = Label(root, text="  Tuesday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Tuesday.grid(row=1, column=3)


Wednesday = Label(root, text="  Wednesday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Wednesday.grid(row=1, column=4)


Thursday = Label(root, text="  Thursday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Thursday.grid(row=1, column=5)


Friday = Label(root, text="  Friday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Friday.grid(row=1, column=6)
#D2FF72

Saturday = Label(root, text="  Saturday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Saturday.grid(row=1, column=7)


Sunday = Label(root, text="  Sunday  ",font=("Arial", "13", "bold"), fg="#D2FF72", bd=0, bg="#624E88")
Sunday.grid(row=1, column=8)

if day_week == "Monday":
    Monday.config(fg="#347928",font=("Arial", "29", "bold"))

elif day_week == "Tuesday":
    Tuesday.config(fg="#347928",font=("Arial", "29", "bold"))


elif day_week == "Wednesday":
    Wednesday.config(fg="#347928",font=("Arial", "29", "bold"))


elif day_week == "Thursday":
    Thursday.config(fg="#347928",font=("Arial", "29", "bold"))


elif day_week == "Friday":
    Friday.config(fg="#347928",font=("Arial", "29", "bold"))


elif day_week == "Saturday":
    Saturday.config(fg="#347928",font=("Arial", "20", "bold"))


elif day_week == "Sunday":
    Sunday.config(fg="#347928",font=("Arial", "20", "bold"))


Weather = Label(root,text="", bg="GRAY", height=30, width=26)
Weather.place(x=968, y=165)

lb2 = Label(root, text=f"weather\n", font=("Arial", 30, "bold"), bg="GRAY", fg="WHITE")
lb2.place(x=983, y=190)

city_weather = Entry(root, font=("Arial" ,20), width=10)
city_weather.place(x=983, y=450)



weather_check = Button(root, text="Check", command=weather, bg="#87A2FF", fg="#001F3F", font=("Arial", "20", "bold"))
weather_check.place(x=1007, y=515)



temp_label = Label(root, text="", font=("Arial", 17), bg="GRAY", fg="CYAN")
temp_label.place(x=980, y=280)

#--------------------------------------------

account_label = Label(root, text="", bg="#D9EAFD", width=67, height=20)
account_label.place(x=415, y=165)

info_label = Label(root, text='', bg="#D9EAFD", font=("Arial", 20, "bold"))
info_label.place(x=420, y=170)

info_label1 = Label(root, text='', bg="#D9EAFD", font=("Arial", 20, "bold"))
info_label1.place(x=420, y=220)

info_label2 = Label(root, text='', bg="#D9EAFD", font=("Arial", 20, "bold"))
info_label2.place(x=420, y=270)

info_label3 = Label(root, text='', bg="#D9EAFD", font=("Arial", 20, "bold"))
info_label3.place(x=420, y=320)

signin_btn = Button(root, text="log in", bg="#FFB200", fg="#EB5B00", font=("Arial", 20, "bold"), bd=0, command=sign_in)
signin_btn.grid(row=2, column=4, columnspan=2, rowspan=2)

#--------------------------------------------

def reviwe():
    with open("data.txt", "r") as read:
        if read != "":
            content = read.read()
            content = content.split(",")
            info_label.config(text=f"Name: {content[0]}")
            info_label1.config(text=f"family Name: {content[1]}")
            info_label2.config(text=f"Age: {content[2]}")
            info_label3.config(text=f"Blood type: {content[3]}")
            signin_btn.destroy()


delcounter = 0

with open("data.txt", "r") as r:
    if r == "":

        sign_in()

    else:

        reviwe()
def delacc():

    with open("data.txt", 'w') as delete:

        global delcounter

        delete.write(",,,,")

        info_label.config(text=",")

        info_label1.config(text=",")

        info_label2.config(text=",")

        info_label3.config(text=",")
        delcounter += 1
        signin_btn = Button(root, text="log in", bg="#FFB200", fg="#EB5B00", font=("Arial", 20, "bold"), bd=0,
                            command=sign_in)
        signin_btn.grid(row=2, column=4, columnspan=2, rowspan=2)




delbtn = Button(root, text="delete account", command=delacc)
delbtn.place(x=420, y=438)

def CompleteClean():
    clean(root, btn_Time, btn_Planner, btn_Notes, btn_Health, line_1, line_2, line_3, line_4)

#-------------------Time-----------------------

#-------------------Planner--------------------





root.mainloop()