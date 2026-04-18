import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    REP = 0
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REP
    REP += 1
    if REP %2 == 0:
        timer_label.config(text="Short Break",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    elif REP % 8 ==0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        rep_count = REP/2
        text = ""
        for n in range(0,rep_count):
            text += "✅",
        check_mark_label.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100,132,text="00:00" , fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start",font=("times new roman",10,"normal"),bg="white",command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",font=("Times new roman",10,"normal"),bg="white", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(text="✅", fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=1)

window.mainloop()