#Program: Python Calculator
#Author: Brent Lang
#Date: 11/30/20
#Purpose: Simple calculator program, program is able to add, subtract, multiply and divide.
#         Calculator is able to utilize positive and negative as well as integer and floating point numbers.

from tkinter import *

expression = ''

#Function updates mathmatical expression in expression_field window
def button_press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 

# Function evaluates expression in expression_field window
# Provides an error if expression can not be evaluated
def equal_press(): 
	try: 
		global expression 
		total = str(eval(expression)) 
		equation.set(total) 
		expression = "" 
	except: 
		equation.set(" Error ") 
		expression = "" 

# Function clears expression_field window
def clear_press(): 
	global expression 
	expression = "" 
	equation.set("") 


# Creates the calculator window and uses lambda functions for various button presses
window = Tk() 

window.title("Calculator") 

window.geometry("400x300")
window.grid_rowconfigure(0, weight = 1)
window.grid_rowconfigure(1, weight = 1)
window.grid_rowconfigure(2, weight = 1)
window.grid_rowconfigure(3, weight = 1)
window.grid_rowconfigure(4, weight = 1)
window.grid_rowconfigure(5, weight = 1)
window.grid_rowconfigure(6, weight = 1)
window.grid_columnconfigure(0, weight = 1)
window.grid_columnconfigure(1, weight = 1)
window.grid_columnconfigure(2, weight = 1)
window.grid_columnconfigure(3, weight = 1)
window.resizable(True,True)

equation = StringVar() 

expression_field = Entry(window, bg = 'Ivory', width = 38, textvariable = equation) 
expression_field.grid(columnspan = 4, rowspan = 2 , padx = 7, sticky = W+E+N+S)
expression_field.grid_columnconfigure(0, weight = 1)

equation.set('') 
 
button1 = Button(window, text = '1', command = lambda: button_press(1), height = 2, width = 10) 
button1.grid(row = 2, column = 0, sticky = W+E+N+S) 

button2 = Button(window, text = '2', command = lambda: button_press(2), height = 2, width = 10) 
button2.grid(row = 2, column = 1, sticky = W+E+N+S) 

button3 = Button(window, text = '3', command = lambda: button_press(3), height = 2, width = 10) 
button3.grid(row = 2, column = 2, sticky = W+E+N+S) 

button4 = Button(window, text = '4', command = lambda: button_press(4), height = 2, width = 10) 
button4.grid(row = 3, column = 0, sticky = W+E+N+S) 

button5 = Button(window, text = '5', command = lambda: button_press(5), height = 2, width = 10) 
button5.grid(row = 3, column = 1, sticky = W+E+N+S) 

button6 = Button(window, text = '6', command = lambda: button_press(6), height = 2, width = 10) 
button6.grid(row = 3, column = 2, sticky = W+E+N+S) 

button7 = Button(window, text = '7', command = lambda: button_press(7), height = 2, width = 10) 
button7.grid(row = 4, column = 0, sticky = W+E+N+S) 

button8 = Button(window, text = '8', command = lambda: button_press(8), height = 2, width = 10) 
button8.grid(row = 4, column = 1, sticky = W+E+N+S) 

button9 = Button(window, text = '9', command = lambda: button_press(9), height = 2, width = 10) 
button9.grid(row = 4, column = 2, sticky = W+E+N+S) 

button0 = Button(window, text = '0', command = lambda: button_press(0), height = 2, width = 10) 
button0.grid(row = 5, column = 0, sticky = W+E+N+S, columnspan = 2) 

plus_button = Button(window, text =  ' + ', command = lambda: button_press("+"), height = 2, width = 10) 
plus_button.grid(row = 2, column = 3, sticky = W+E+N+S)

minus_button = Button(window, text = ' - ', command = lambda: button_press("-"), height = 2, width = 10) 
minus_button.grid(row = 3, column = 3, sticky = W+E+N+S) 

multiply_button = Button(window, text = ' * ', command = lambda: button_press("*"), height = 2, width = 10) 
multiply_button.grid(row = 4, column = 3, sticky = W+E+N+S) 

divide_button = Button(window, text = ' / ', command = lambda: button_press("/"), height = 2, width = 10) 
divide_button.grid(row = 5, column = 3, sticky = W+E+N+S) 

equal_button = Button(window, text = ' = ', command = equal_press, height = 2, width = 10) 
equal_button.grid(row = 6, column = 0, sticky = W+E+N+S, columnspan = 3) 

clear_button = Button(window, text = 'Clear', command = clear_press, height = 2, width = 10) 
clear_button.grid(row = 6, column = 3, sticky = W+E+N+S) 

decimal_button = Button(window, text = '.', command = lambda: button_press('.'), height = 2, width = 10) 
decimal_button.grid(row = 5, column = 2, sticky = W+E+N+S) 

window.mainloop() 