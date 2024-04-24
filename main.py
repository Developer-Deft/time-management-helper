from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timers = ""
marks = ""


# -------------------- -------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timers)
    my_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it is the 8th reps
    if reps % 8 == 0:
        my_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # if it is 2nd/4th/6th reps
    elif reps % 2 == 0:
        my_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # if it is 1st/3rd/5th/7th reps
        my_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    # 01:45
    # 300 / 60 = 5 minute
    # 245 = 4 minute
    # 245 % 4 = seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # elif count_sec < 10:
    #     conversion = str(count_sec)
    #     count_sec = f"0{conversion}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timers
        timers = window.after(1000, count_down, count - 1)
        winsound.Beep(1000, 100)

    else:
        start_countdown()
        global marks
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks = "✔"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW, highlightthickness=0)


fg = GREEN
my_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=fg, bg=YELLOW)
my_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg="white", borderwidth=0, command=start_countdown)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", highlightthickness=0, bg="white", borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=fg, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
