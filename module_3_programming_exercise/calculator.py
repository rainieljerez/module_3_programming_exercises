#Use tkinter as the ui of the calculator

import tkinter as tk
from tkinter import messagebox

#Calculator math functions
def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        raise ValueError ("Cannot divide by zero")
    return num_1 / num_2

def calculate(operations, num_1, num_2):
    ops = {
        "Addition": (add, "+"),
        "Subtraction": (subtract, "-"),
        "Multiplication": (multiply, "*"),
        "Division": (divide, "/")
    }
    func, symbol =ops[operations]
    return symbol, func(num_1, num_2)
#Returns a float value
def format_result(value):
    return f"{float(value):.10g}"

