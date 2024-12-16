#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите простейший калькулятор, состоящий из двух текстовых полей,
# куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
# Результат вычисления должен отображаться в метке. Если арифметическое действие
# выполнить невозможно (например, если были введены буквы, а не числа),
# то в метке должно появляться слово "ошибка".

import tkinter as tk


def calc(func: str, entry_1: tk.Entry, entry_2: tk.Entry, lable: tk.Label) -> None:
    try:
        num_1 = int(entry_1.get())
        num_2 = int(entry_2.get())
    except ValueError:
        lable.config(text="Ошибка")
        return

    match func:
        case "+":
            lable.config(text=num_1 + num_2)
        case "-":
            lable.config(text=num_1 - num_2)
        case "*":
            lable.config(text=num_1 * num_2)
        case "/":
            lable.config(text=num_1 / num_2)


if __name__ == "__main__":
    root = tk.Tk()

    entry_1 = tk.Entry(root)
    entry_1.pack(padx=30)

    entry_2 = tk.Entry(root)
    entry_2.pack(padx=30)
    lable = tk.Label(root, text="")

    plus = tk.Button(root, text="+", command=lambda: calc("+", entry_1, entry_2, lable))
    plus.pack(padx=20, fill="x")

    minus = tk.Button(
        root, text="-", command=lambda: calc("-", entry_1, entry_2, lable)
    )
    minus.pack(padx=20, fill="x")

    mul = tk.Button(root, text="*", command=lambda: calc("*", entry_1, entry_2, lable))
    mul.pack(padx=20, fill="x")

    div = tk.Button(root, text="/", command=lambda: calc("/", entry_1, entry_2, lable))
    div.pack(padx=20, fill="x")

    lable.pack()

    root.mainloop()
