#Use tkinter as the ui of the calculator

import tkinter as tk
from tkinter import messagebox
import math

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

def floor_division(num_1, num_2):
    if num_2 == 0:
        raise ValueError ("Cannot divide by zero")
    return num_1 // num_2

def modulus (num_1, num_2):
    if num_2 == 0:
        raise ValueError ("Cannot modulo by zero")
    return num_1 % num_2

def power (num_1, num_2):
    return num_1 ** num_2

def square_root(num_1, _):
    if num_1 < 0:
        raise ValueError ("Cannot take the square root of a negative number")
    return math.sqrt(num_1)

def cube_root (num_1, _):
    return math.copysign(abs(num_1) ** (1/3), num_1)

OPERATIONS = {
    "Addition": (add, "+", True),
    "Subtraction": (subtract, "-", True),
    "Multiplication": (multiply, "*", True),
    "Division": (divide, "/", True),
    "Floor Division": (floor_division, "//", True),
    "Modulus": (modulus, "%", True),
    "Exponent": (power, "**", True),
    "Square Root": (square_root, "sqrt", False),
    "Cube Root": (cube_root, "cbrt", False),
}

def calculate(operation, num_1, num_2):

    func, symbol, _ = OPERATIONS[operation]
    return symbol, func(num_1, num_2)
#Returns a float value
def format_result(value):
    return f"{float(value):.10g}"

class SimpleCalculatorApp(tk. Tk):
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
        self.resizable(width = False, height = False)
        self.configure(bg = self.BG)
        self._build_ui()
        self._center_window(500,600)

    def _build_ui(self):
        pad = dict(padx = 24, pady = 6)

        tk.Label(
            self, text="Calculator", bg = self.BG, fg = self.WHITE,
            font = ("Segoe UI", 18, "bold")).pack(pady = (28, 4))

        tk.Label(
            self, text="Choose an operation and enter two numbers",
            bg=self.BG, fg=self.SUBTEXT,
            font=("Segoe UI", 10)).pack(pady=(0, 16))

        tk.Label(
            self, text = "Operations", bg = self.BG, fg = self.SUBTEXT,
            font = ("Segoe UI", 9, "bold"), anchor = "w").pack(fill = "x", **pad)

        self.operation_var = tk.StringVar(value = "Addition")
        self.operation_var.trace_add("write", self._on_operation_change)

        operation_names = list(OPERATIONS.keys())
        dropdown= tk.OptionMenu(self, self.operation_var, *operation_names)
        dropdown.config(
            bg = self.PANEL, fg = self.WHITE, activebackground = self.ACCENT,
            activeforeground = self.WHITE, font = ("Segoe UI", 11),
            relief = "flat", bd = 0, highlightthickness = 0,
            indicatoron = True, anchor = "w", width = 36
        )
        dropdown ["menu"].config(
            bg = self.PANEL, fg = self.WHITE, activebackground = self.ACCENT,
            activeforeground = self.WHITE, font = ("Segoe UI", 10),
            relief = "flat"
        )
        dropdown.pack(fill = "x", padx = 24, pady = (0,10))


        self.num1_var = tk.StringVar()
        self._make_input(pad, "First Number", self.num1_var)

        self.num2_var = tk.StringVar()
        self.num2_label = tk.Label(self, text = "Second Number", bg = self.BG,
                                   fg = self.SUBTEXT, font = ("Segoe UI", 9, "bold"),
                                   anchor = "w")
        self.num2_label.pack(fill = "x", **pad)
        self.num2_entry = tk.Entry(
            self, textvariable = self.num2_var,
            bg = self.PANEL, fg  =self.WHITE, insertbackground = self.WHITE,
            relief = "flat", font = ("Segoe UI", 13),
            highlightthickness = 2, highlightbackground = self.PANEL,
            highlightcolor = self.ACCENT,
        )
        self.num2_entry.pack(fill = "x", padx = 24, pady = (0,8), ipadx = 6, ipady = 8)

        tk.Button(
            self, text = "Calculate",
            bg = self.ACCENT, fg = self.WHITE,
            activebackground = self.ACCENT_DARK, activeforeground = self.WHITE,
            font = ("Segoe UI", 12, "bold"),
            relief = "flat", cursor = "hand2", bd = 0,
            padx = 18, pady = 10,
            command = self._on_calculate
        ).pack(pady = (14,8))

        result_frame = tk.Frame(self, bg = self.PANEL, bd = 0)
        result_frame.pack(fill = "x", padx = 24, pady = 8)

        tk.Label(result_frame, text = "Result", bg = self.PANEL, fg = self.SUBTEXT,
            font = ("Segoe UI", 9, "bold"),).pack (anchor = "w", padx = 14, pady = (10, 2))

        self.result_label = tk.Label(
            result_frame, text = "-",
            bg = self.PANEL, fg = self.SUCCESS,
            font = ("Segoe UI", 15, "bold"),
            wraplength = 440,
            justify = "left",
            anchor = "w"
        )
        self.result_label.pack(anchor = "w", padx = 14, pady = (0, 16))

        button_row = tk.Frame(self, bg = self.BG)
        button_row.pack(pady = (8, 0))

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
            font = ("Segoe UI", 10), relief = "flat", cursor = "hand2",
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
            highlightcolor = self.ACCENT,
        )
        entry.pack(fill = "x", padx = 24, pady = (0,8), ipadx =6, ipady = 8)
#second number depends on the operation chosen
    def _on_operation_change(self, *_):
        operation_2nd_num = self.operation_var.get()
        _,_, needs_second = OPERATIONS.get(operation_2nd_num, (None, None, True))
        state = "normal" if needs_second else "disabled"
        self.num2_entry.config(state = state)
        fg_color = self.SUBTEXT if needs_second else "#555570"
        self.num2_label.config(fg=fg_color)
        if not needs_second:
            self.num2_var.set("-")
        else:
            if self.num2_var.get() == "-":
                self.num2_var.set("")
#exception handlers
#ensures that input should be numbers only
#perform calculation
    def _on_calculate(self):
        try:
            num_1 = float(self.num1_var.get().strip())
        except ValueError:
            self._show_error("First input is invalid. Enter a numerical value")
            return
        operation_2nd_num = self.operation_var.get()
        _, _, needs_second = OPERATIONS[operation_2nd_num]
        if needs_second:
            try:
                num_2 = float(self.num2_var.get().strip())
            except ValueError:
                self._show_error("Second input is invalid. Enter a numerical value")
                return
        else:
            num_2 = 0.0
        try:
            symbol, result = calculate(operation_2nd_num, num_1, num_2)
            formatted = f"{float(result):.4f}"
            if needs_second:
                expression = f"{float(num_1):.4f} {symbol} {float(num_2):.4f} = {formatted}"
            else:
                expression = f"{symbol}({float(num_1):.4f}) = {formatted}"
            self.result_label.config(text=expression, fg=self.SUCCESS)
        except ValueError as e:
            self._show_error(str(e))

    def _on_try_again(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.operation_var.set("Addition")
        self.result_label.config(text = "-", fg = self.SUCCESS)

    def _on_exit(self):
        messagebox.showinfo("Exiting Program", "Thank you for using the Simple Calculator App")
        self.destroy()

    def _show_error(self, message):
        self.result_label.config(text = f"{message}", fg = self.ERROR)
        messagebox.showerror("Input Error", message)

    def _center_window(self, w, h):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == "__main__":
    app = SimpleCalculatorApp()
    app.mainloop()




