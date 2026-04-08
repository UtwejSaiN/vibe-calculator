#!/usr/bin/env python3
"""
Amazing Calculator - GUI Version
"""

import tkinter as tk
from tkinter import font


class AmazingCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Amazing Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')

        # Variables
        self.current_input = ""
        self.operator = ""
        self.first_number = None

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_font = font.Font(family='Arial', size=24, weight='bold')
        title_label = tk.Label(
            self.root,
            text="✨ Amazing Calculator ✨",
            font=title_font,
            bg='#1a1a2e',
            fg='#00d4ff',
            pady=20
        )
        title_label.pack()

        # Display Frame
        display_frame = tk.Frame(self.root, bg='#1a1a2e')
        display_frame.pack(pady=10)

        # Display
        display_font = font.Font(family='Arial', size=28, weight='bold')
        self.display = tk.Entry(
            display_frame,
            font=display_font,
            bg='#16213e',
            fg='#ffffff',
            justify='right',
            bd=0,
            insertbackground='#00d4ff',
            width=15
        )
        self.display.pack(padx=20, pady=10, ipady=15)
        self.display.insert(0, "0")

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg='#1a1a2e')
        buttons_frame.pack(pady=10)

        # Button styling
        button_font = font.Font(family='Arial', size=18, weight='bold')

        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        # Button colors
        number_color = '#0f3460'
        operator_color = '#e94560'
        special_color = '#533483'
        equals_color = '#00d4ff'

        # Create buttons
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                # Determine button color
                if btn_text in ['C', '⌫', '%']:
                    bg_color = special_color
                elif btn_text in ['+', '-', '*', '/']:
                    bg_color = operator_color
                elif btn_text == '=':
                    bg_color = equals_color
                else:
                    bg_color = number_color

                # Special width for 0 and =
                if btn_text == '0':
                    btn = tk.Button(
                        buttons_frame,
                        text=btn_text,
                        font=button_font,
                        bg=bg_color,
                        fg='#ffffff',
                        activebackground='#00d4ff',
                        activeforeground='#1a1a2e',
                        bd=0,
                        width=11,
                        height=2,
                        command=lambda x=btn_text: self.button_click(x)
                    )
                    btn.grid(row=i, column=j, columnspan=2, padx=5, pady=5, sticky='ew')
                elif btn_text == '=':
                    btn = tk.Button(
                        buttons_frame,
                        text=btn_text,
                        font=button_font,
                        bg=bg_color,
                        fg='#1a1a2e',
                        activebackground='#ffffff',
                        activeforeground='#1a1a2e',
                        bd=0,
                        width=5,
                        height=2,
                        command=lambda x=btn_text: self.button_click(x)
                    )
                    btn.grid(row=i, column=j, columnspan=2, padx=5, pady=5, sticky='ew')
                else:
                    btn = tk.Button(
                        buttons_frame,
                        text=btn_text,
                        font=button_font,
                        bg=bg_color,
                        fg='#ffffff',
                        activebackground='#00d4ff',
                        activeforeground='#1a1a2e',
                        bd=0,
                        width=5,
                        height=2,
                        command=lambda x=btn_text: self.button_click(x)
                    )
                    btn.grid(row=i, column=j, padx=5, pady=5)

        # Footer
        footer_font = font.Font(family='Arial', size=10)
        footer_label = tk.Label(
            self.root,
            text="Where Math Meets Aesthetic",
            font=footer_font,
            bg='#1a1a2e',
            fg='#00d4ff'
        )
        footer_label.pack(side='bottom', pady=10)

    def button_click(self, value):
        if value == 'C':
            # Clear everything
            self.current_input = ""
            self.operator = ""
            self.first_number = None
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")

        elif value == '⌫':
            # Backspace
            current = self.display.get()
            if len(current) > 1:
                self.display.delete(0, tk.END)
                self.display.insert(0, current[:-1])
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")

        elif value in ['+', '-', '*', '/', '%']:
            # Operator
            try:
                self.first_number = float(self.display.get())
                self.operator = value
                self.current_input = ""
                self.display.delete(0, tk.END)
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif value == '=':
            # Calculate
            try:
                if self.first_number is not None and self.operator:
                    second_number = float(self.display.get())
                    result = self.calculate(self.first_number, self.operator, second_number)
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    self.first_number = None
                    self.operator = ""
            except (ValueError, ZeroDivisionError) as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        else:
            # Number or decimal
            current = self.display.get()
            if current == "0" or current == "Error":
                self.display.delete(0, tk.END)
                self.display.insert(0, value)
            else:
                # Prevent multiple decimals
                if value == '.' and '.' in current:
                    return
                self.display.delete(0, tk.END)
                self.display.insert(0, current + value)

    def calculate(self, num1, op, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return num1 / num2
        elif op == '%':
            return num1 % num2
        return 0


def main():
    root = tk.Tk()
    app = AmazingCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
