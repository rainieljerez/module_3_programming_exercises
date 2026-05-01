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
    func, symbol = ops[operations]
    return symbol, func(num_1, num_2)
#Returns a float value
def format_result(value):
    return f"{float(value):.10g}"

class Calculator(tk. Tk):
#color of the ui
    BG = "#1e1e2e"
    PANEL = "#2a2a3d"
    ACCENT = "#7c6af7"
    ACCENT_DARK = "#5a4fcf"
    TEXT = "#e0e0f0"
    SUBTEXT = "#9090b0"
    SUCCESS = "#4caf8a"
    ERROR = "#e06c75"
    WHITE = "#ffffff"

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(width=False, height=False)
        self.configure(bg=self.BG)

        self._build_ui()
        self._center_window(420, 560)

    def _build_ui(self):
        pad = dict(padx=24, pady=8)

        tk.Label(
            self, text="Calculator",
            bg = self.BG,
            fg = self.WHITE,
            font = ("Segoe UI", 18, "bold")
        ).pack(pady = (28, 4))

        

