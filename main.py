from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
work=0
period="work"
timer=None
checkmarkString = ""
# ---------------------------- TIMER RESET ------------------------------- # 

def resetTimer():
    global timer
    global checkmarkString
    global reps
    if timer is not None:
        try:
            # print("abc")
            # print(timer)
            window.after_cancel(timer)
            canvas.itemconfig(timer_text, text="00:00")
            label.config(text="Timer")
            checkmarkString=""
            reps=0

        except ValueError:
            print("Timer ID was invalid.")
        timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, checkmarkString
    reps += 1
    if reps%8==0:
        label.config(text="long break")
        count_down(20*60)
    elif reps%2==0:
        label.config(text="5 minute break")
        count_down(5*60)
    else:
        label.config(text="work work work")
        count_down(25 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

def count_down(count):
    global reps
    global timer
    global checkmarkString
    minutes= math.floor(count/60)
    seconds=count%60
    if len(str(seconds))==1:
        seconds="0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count>0:
        timer=window.after(1000, count_down, count-1)
        # print(type (timer))
    if count==0:
        start_timer()
        workSessions=math.floor(reps/2)

        for _ in range(workSessions):
            checkmarkString +="c"
        label1.config(text=checkmarkString)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# def refresh_method(thing):
#     print(thing)
# window.after(1000, refresh_method, "hello")#hello is the parameter of the function that is called.



canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)



label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label.grid(column=1, row=0)

label1=Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label1.grid(column=1, row=4)

button1=Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
button1.grid(column=0, row=2)

button2=Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=resetTimer)
button2.grid(column=2, row=2)

window.mainloop()