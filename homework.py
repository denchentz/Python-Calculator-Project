from tkinter import *
import os.path
import json

window = Tk()

window.title("Calculator")

window.resizable(width=False, height=False)

window.geometry('500x600')
'''
class History():
    def __init__(self):
        self.index = 0
        self.record = []
        self.display_list = []

    def history_read(self):
        file_path = "history.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                json_str = file.read()
                self.record = json.loads(json_str)
                self.index = len(self.record)

    def history_write(self):
        file_path = "history.txt"
        with open(file_path, 'w') as file:
            json_str = json.dumps(self.record)
            file.write(json_str)
    
    def history_record(self, i: int) -> str:
        if self.record[i]["type"] == 2:
            num1 = self.record[i]["num1"]
            operator = self.record[i]["operator"]
            num2 = self.record[i]["num2"]
            result = self.record[i]["result"]
            return f"{num1} {operator} {num2} = {result}"

    def history_record_result(self, i: int) -> str:
        result = self.record[i]["result"]
        return result

    def history_append(self, type: int, num1: str, operator: str, num2: str, result: str):
        if self.index >= 100:
            self.record.pop([0])
            self.index = 99
        if type == 2:
            self.record[self.index]["type"] = type
            self.record[self.index]["num1"] = num1
            self.record[self.index]["operator"] = operator
            self.record[self.index]["num2"] = num2
            self.record[self.index]["result"] = result
        self.index += 1
        return


'''
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
        self.index = 0
        self.record = []
        self.display_list = []

    def history_read(self):
        file_path = "history.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                json_str = file.read()
                self.record = json.loads(json_str)
                self.index = len(self.record)

    def history_write(self):
        file_path = "history.txt"
        with open(file_path, 'w') as file:
            json_str = json.dumps(self.record)
            file.write(json_str)

    def history_record(self, i: int) -> str:
        if self.record[i]["type"] == 2:
            num1 = self.record[i]["num1"]
            operator = self.record[i]["operator"]
            num2 = self.record[i]["num2"]
            result = self.record[i]["result"]
            return f"{num1} {operator} {num2} = {result}"

    def history_record_result(self, i: int) -> str:
        result = self.record[i]["result"]
        return result

    def history_append(
            self, type: int, num1: str, operator: str, num2: str, result: str):
        if self.index >= 100:
            self.record.pop([0])
            self.index = 99
        if type == 2:
            self.record[self.index]["type"] = type
            self.record[self.index]["num1"] = num1
            self.record[self.index]["operator"] = operator
            self.record[self.index]["num2"] = num2
            self.record[self.index]["result"] = result
        self.index += 1
        return

    def numberEnter(self, num):
        self.result = False
        firstnum = textbox.get()
        secondnum = str(num)
        if self.input_value:
            if secondnum == '0':
                return
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(textbox.get())

    def display(self, value):
        textbox.delete(0, END)
        textbox.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.history_append(
                2, str(self.total),
                "+", str(self.current),
                str(self.total + self.current))
            self.total += self.current
        if self.op == "sub":
            self.history_append(
                type=2, num1=str(self.total),
                operator="-", num2=str(self.current),
                result=str(self.total - self.current))
            self.total -= self.current
        if self.op == "multi":
            self.history_append(
                type=2, num1=str(self.total),
                operator="x", num2=str(self.current),
                result=str(self.total * self.current))
            self.total *= self.current
        if self.op == "divide":
            if self.current == 0:
                textbox.delete(0, END)
                textbox.insert(0, "ERROR")
                self.input_value = True
                self.check_sum = False
                return
            self.history_append(
                type=2, num1=str(self.total),
                operator=chr(247), num2=str(self.current),
                result=str(self.total / self.current))
            self.total /= self.current
        #if self.op == "%":
        #    self.total = (self.total/100) + "%"
        if self.op == "+/-":
            self.total *= -1
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def All_Clear_Entry(self):
        self.result = False
        self.current = ''
        self.display(0)
        self.input_value = True
        self.total = 0

added_value = Calc()
added_value.history_read()
# Display

textbox = Entry(window,
                font=('Arial', 20, 'bold'),
                bd=30, width=28,
                justify=RIGHT)

textbox.grid(row=0,
             column=0,
             columnspan=4)

textbox.insert(0, "0")

# Number Button
number = "789456123"
i = 0
btn_list = []
for r in range(2, 5):
    for c in range(3):
        btn_list.append(Button(window,
                               width=6,
                               height=2,
                               font=('Arial', 20, 'bold'),
                               bd=4, text=number[i]))
        btn_list[i].grid(row=r, column=c, pady=1)
        btn_list[i]["command"] = lambda x=number[i]: added_value.numberEnter(x)
        i += 1

# Operating Button

btnAllClear = Button(window, text="AC",
                     width=6, height=2,
                     font=('Arial', 20, 'bold'), bd=4,
                     command=lambda: added_value.All_Clear_Entry())                      
btnAllClear.grid(row=1, column=0, pady=1)

btnNegative = Button(window, text="+/-",
                     width=6, height=2,
                     font=('Arial', 20, 'bold'), bd=4,
                     command=lambda: added_value.operation("+/-"))
btnNegative.grid(row=1, column=1, pady=1)

btnPercentage = Button(window, text="%",
                    width=6, height=2,
                    font=('Arial', 20, 'bold'), bd=4,
                    command=lambda: added_value.operation("%"))
btnPercentage.grid(row=1, column=2, pady=1)

btnDivide = Button(window, text=chr(247),
                width=6, height=2,
                font=('Arial', 20, 'bold'), bd=4,
                command=lambda: added_value.operation("divide"))
btnDivide.grid(row=1, column=3, pady=1)

btnMulti = Button(window, text="x",
                width=6, height=2,
                font=('Arial', 20, 'bold'), bd=4,
                command=lambda: added_value.operation("multi"))
btnMulti.grid(row=2, column=3, pady=1)

btnSub = Button(window, text="-",
                width=6, height=2,
                font=('Arial', 20, 'bold'), bd=4,
                command=lambda: added_value.operation("sub"))
btnSub.grid(row=3, column=3, pady=1)

btnAdd = Button(window, text="+",
                width=6, height=2,
                font=('Arial', 20, 'bold'), bd=4,
                command=lambda: added_value.operation("add"))
btnAdd.grid(row=4, column=3, pady=1)

btnZero = Button(window, text="0",
                 width=14, height=2,
                 font=('Arial', 20, 'bold'), bd=4,
                 command=lambda: added_value.numberEnter(0))
btnZero.grid(row=6, column=0, columnspan=2, pady=1)

btnDot = Button(window, text=".",
                width=6, height=2,
                font=('Arial', 20, 'bold'), bd=4,
                command=lambda: added_value.numberEnter("."))
btnDot.grid(row=6, column=2, pady=1)

btnEqual = Button(window, text="=",
                  width=6, height=2,
                  font=('Arial', 20, 'bold'), bd=4,
                  command=added_value.sum_of_total)
btnEqual.grid(row=6, column=3, pady=1)

btnHistory = Button(window, text="History",
                    width=31, height=2,
                    font=('Arial', 20, 'bold'), bd=4)
btnHistory.grid(row=7, column=0, columnspan=4, pady=1)

window.mainloop()

added_value.history_write()