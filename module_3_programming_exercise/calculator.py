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

def calculate(operation, num_1, num_2):
    ops = {
        "Addition": (add, "+"),
        "Subtraction": (subtract, "-"),
        "Multiplication": (multiply, "*"),
        "Division": (divide, "/")
    }
    func, symbol = ops[operation]
    return symbol, func(num_1, num_2)
#Returns a float value
def format_result(value):
    return f"{float(value):.10g}"

class Calculator(tk. Tk):
#elements of the ui
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
        self._center_window(420,560)

    def _build_ui(self):
        pad = dict(padx=24, pady=8)

        tk.Label(
            self, text="Calculator",
            bg = self.BG,
            fg = self.WHITE,
            font = ("Segoe UI", 18, "bold")
        ).pack(pady = (28, 4))

        tk.Label(
            self, text="Choose an operation and enter two numbers",
            bg=self.BG, fg=self.SUBTEXT,
            font=("Segoe UI", 10)
        ).pack(pady=(0, 16))

        tk.Label(
            self, text = "Operations",
            bg = self.BG, fg = self.SUBTEXT,
            font = ("Segoe UI", 9, "bold"), anchor = "w"
        ).pack(fill = "x", **pad)

        self.operation_var = tk.StringVar(value = "Addition")
        op_frame = tk.Frame(self, bg = self.PANEL, bd = 0)
        op_frame.pack(fill = "x", padx = 24, pady = (0,12))

        operations = [
            ("➕  Addition", "Addition"),
            ("➖  Subtraction", "Subtraction"),
            ("✖️  Multiplication", "Multiplication"),
            ("➗  Division", "Division"),
        ]
        for col, (label, value) in enumerate(operations):
            rb = tk.Radiobutton(
                op_frame, text = label, variable = self.operation_var, value = value,
                bg = self.PANEL, fg = self.TEXT, selectcolor = self.ACCENT,
                activebackground = self.PANEL, activeforeground = self.WHITE,
                font = ("Segoe UI", 10), indicatoron = True, bd = 0,
                highlightthickness = 0
            )
            rb.grid(row = col // 2, column = 2, sticky = "w", padx =12, pady = 6)

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()

        self._make_input(pad, "First Number", self.num1_var)
        self._make_input(pad, "Second Number", self.num2_var)

        tk.Button(
            self, text = "Calculate",
            bg = self.ACCENT, fg = self.WHITE,
            activebackground = self.ACCENT_DARK, activeforeground = self.WHITE,
            font = ("Segoe UI", 12, "bold"),
            relief = "flat", cursor = "hand2", bd = 0,
            padx = 18, pady = 10,
            command = self._on_calculate
        ).pack(pady = (18,10))

        result_frame = tk.Frame(self, bg = self.PANEL, bd = 0)
        result_frame.pack(fill = "x", padx = 24, pady = 8)

        tk.Label(
            result_frame, text = "Result",
            bg = self.PANEL, fg = self.SUBTEXT,
            font = ("Segoe UI", 9, "bold"),
        ).pack (anchor = "w", padx = 14, pady = (10, 2))

        self.result_label = tk.Label(
            result_frame, text = "-",
            bg = self.PANEL, fg = self.SUCCESS,
            font = ("Segeo UI", 22, "bold")
        )
        self.result_label.pack(anchor = "w", padx = 14, pady = (0, 12))

        button_row = tk.Frame(self, bg = self.BG)
        button_row.pack(pady = (10, 0))

        tk.Button(
            button_row, text = "Try Again",
            bg = self.PANEL, fg =self.TEXT,
            activebackground = self.ACCENT, activeforeground = self.WHITE,
            font = ("Segoe UI", 10), relief = "flat", cursor = "hand2",
            padx = 14, pady = 8,
            command = self._on_try_again
        ). pack(side = "left", padx = 8)

        tk.Button(
            button_row, text = "Exit",
            bg = self.PANEL, fg = self.TEXT,
            activebackground = self.ERROR, activeforeground = self.WHITE,
            font = ("Segou UI", 10), relief = "flat", cursor = "hand2",
            padx = 14, pady = 8,
            command = self._on_exit
        ).pack (side = "left", padx = 8)

    def _make_input(self, pad, label_text, textvariable):
        tk.Label(
            self, text = label_text,
            bg = self.BG, fg = self.SUBTEXT,
            font = ("Segoe UI", 9, "bold"), anchor = "w"
        ).pack(fill = "x", **pad)

        entry = tk.Entry(
            self, textvariable = textvariable,
            bg = self.PANEL, fg = self.WHITE, insertbackground = self.WHITE,
            relief = "flat", font = ("Segoe UI", 13),
            highlightthickness = 2,
            highlightbackground = self.PANEL,
            highlighcolor = self.ACCENT,
        )
        entry.pack(fill = "x", padx = 24, pady = (0,8), ipadx =6, ipady = 8)

        





