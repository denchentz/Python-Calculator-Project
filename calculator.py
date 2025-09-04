import json
import os.path
from tkinter import *

# main window
window = Tk()
window.title("Calculator")
window.resizable(width=False, height=False)
window.geometry('500x560')

expression = ""
total = ""
display = StringVar()
last_display = StringVar()
last_result = ""
history_list = []
end_calculation = True
first_calculation = True

def save_history():
    global history_list, last_result
    if len(history_list) > 99:
        history_list.pop(0)
    history_list.append(last_result)
    
def read_history():
    global history_list
    file_path = "history.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            history_list = json.loads(file.read())

def write_history():
    global history_list
    file_path = "history.txt"
    with open(file_path, 'w') as file:
        json_array = json.dumps(history_list)
        file.write(json_array)
    window.destroy()


def open_history():
    # history window
    history_window = Tk()
    history_window.title("History")
    history_window.resizable(width=False, height=False)
    history_window.geometry('350x405')

    def select():
        global expression, total, first_calculation, end_calculation
        string = history_list_box.get(history_list_box.curselection())
        i = 0
        while True:
            if string[i] == "=": 
                break
            i += 1
        last_display.set(string[0:i] + " =")
        display.set(string[(i+1):len(string)])
        expression = string[(i+1):len(string)]
        total = string[(i+1):len(string)]
        first_calculation = False
        end_calculation = True
        history_window.destroy()

    def clear_history():
        global history_list
        len = history_list_box.size()
        for i in range(len):
            history_list_box.delete(0)
        history_list = []

    # History List Box
    global history_list  # font=("Arial", 14, "bold")
    history_list_box = Listbox(history_window, width=37, height=20, selectmode="single",
                               )
    history_list_box.grid(row=0, column=0, columnspan=2)
    for results in history_list:
        history_list_box.insert(END, results)
    file_scroll = Scrollbar(history_window, orient='vertical',
                            command=history_list_box.yview)
    history_list_box['yscrollcommand'] = file_scroll.set
    
    btnClearHistory = Button(history_window, text="Clear History", width=13, height=1,
                             font=('Arial', 14, 'bold'), command=clear_history)
    btnClearHistory.grid(row=1, column=0)
    btnSelect = Button(history_window, text="Select", width=13, height=1,
                       font=('Arial', 14, 'bold'), command=select)
    btnSelect.grid(row=1, column=1)


    history_window.mainloop()


def press_operation(op):
    global expression, first_calculation, end_calculation
    end_calculation = False
    expression += str(op)
    display.set(expression)
    if first_calculation == False:
        last_display.set("Last Ans = " + total)

def press_num(num):
    global expression, end_calculation, first_calculation
    if num == 0 and expression == "0":
        return
    if end_calculation:
        expression = ""
        end_calculation = False
    expression += str(num)
    display.set(expression)
    if first_calculation == False:
        last_display.set("Last Ans = " + total)

def negative():
    global expression
    if expression == "":
        return
    expression = str(eval(expression)*(-1))
    display.set(expression)
    if first_calculation == False:
        last_display.set("Last Ans = " + total)

def backspace():
    global expression, end_calculation
    if expression == "":
        return
    expression = expression[:-1]
    display.set(expression)
    if expression == "":
        display.set("0")

def press_equal():
    try:
        global expression, last_result, end_calculation, total, first_calculation
        total = str(eval(expression))
        display.set(total)
        last_display.set(f"{expression} =")
        last_result = f"{expression} = {total}"
        save_history()
        expression = total
        end_calculation = True
        first_calculation = False
    except:
        display.set(" error ")
        expression = ""

def all_clear():
    global expression, end_calculation, first_calculation
    expression = ""
    display.set("0")
    end_calculation = True
    if first_calculation == False:
        last_display.set("Last Ans = " + total)

read_history()

# Display
#last = Label(window, text="last calculation: ", font=("Arial", 10))
last_textbox = Entry(window, font=('Arial', 18, 'bold'), width=35, justify=RIGHT)
last_textbox["textvariable"] = last_display
last_textbox.grid(row=0, column=0, columnspan=4, sticky="e")
last_textbox.insert(0, "")

textbox = Entry(window, font=('Arial', 36, 'bold'), width=18, justify=RIGHT)
textbox["textvariable"] = display
textbox.grid(row=1, column=0, columnspan=4)
textbox.insert(0, "0")

# Number Button
number = "789456123"
i = 0
btn_list = []
for r in range(3, 6):
    for c in range(3):
        btn_list.append(Button(window, width=6, height=2, font=('Arial', 20, 'bold'), text=number[i]))
        btn_list[i].grid(row=r, column=c)
        btn_list[i]["command"] = lambda x=number[i]: press_num(x)
        i += 1

# Operating Button

btnAllClear = Button(window, text="AC", width=6, height=2,
                     font=('Arial', 20, 'bold'),command=all_clear)
btnAllClear.grid(row=2, column=0)

btnBackspace = Button(window, text="Backspace", width=9, height=3,
                      font=('Arial', 13, 'bold'), command=backspace)
btnBackspace.grid(row=2, column=1)

btnNegative = Button(window, text="+/-", width=6, height=2, 
                     font=('Arial', 20, 'bold'), command=negative)
btnNegative.grid(row=2, column=2)

btnDivide = Button(window, text=chr(247), width=6, height=2,
                   font=('Arial', 20, 'bold'), command=lambda: press_operation("/"))
btnDivide.grid(row=2, column=3)

btnMulti = Button(window, text=chr(215), width=6, height=2,
                  font=('Arial', 20, 'bold'), command=lambda: press_operation("*"))
btnMulti.grid(row=3, column=3)

btnSub = Button(window, text="-", width=6, height=2,
                font=('Arial', 20, 'bold'), command=lambda: press_operation("-"))
btnSub.grid(row=4, column=3)

btnAdd = Button(window, text="+", width=6, height=2,
                font=('Arial', 20, 'bold'), command=lambda: press_operation("+"))
btnAdd.grid(row=5, column=3)

btnZero = Button(window, text="0", width=14, height=2,
                 font=('Arial', 20, 'bold'), command=lambda: press_num(0))
btnZero.grid(row=7, column=0, columnspan=2)

btnDot = Button(window, text=".", width=6, height=2,
                font=('Arial', 20, 'bold'), command=lambda: press_num("."))
btnDot.grid(row=7, column=2)

btnEqual = Button(window, text="=", width=6, height=2,
                  font=('Arial', 20, 'bold'), command=press_equal)
btnEqual.grid(row=7, column=3)

btnHistory = Button(window, text="History",
                    width=31, height=2,
                    font=('Arial', 20, 'bold'), command=open_history)
btnHistory.grid(row=8, column=0, columnspan=4)


window.protocol("WM_DELETE_WINDOW", write_history)
window.mainloop()