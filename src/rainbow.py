#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
# соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое
# поле должен ставляться код цвета, а в метку – название цвета. Коды цветов в
# шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
# #ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий,
# #7d00ff – фиолетовый.

import tkinter as tk
from functools import partial


def calc(color: str, entry: tk.Entry, lable: tk.Label) -> None:
    lable.config(text=color)
    entry.delete(0, "end")
    entry.insert(0, colors[color])


if __name__ == "__main__":
    root = tk.Tk()

    lable = tk.Label(root, text="")
    lable.pack()
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=10)

    colors: dict[str, str] = {
        "Красный": "#ff0000",
        "Оранжевый": "#ff7d00",
        "Желтый": "#ffff00",
        "Зеленый": "#00ff00",
        "Голубой": "#007dff",
        "Синий": "#0000ff",
        "Фиолетовый": "#7d00ff",
    }

    for color in colors:
        tk.Button(
            root,
            text="",
            bg=colors[color],
            command=partial(calc, color, entry, lable),
        ).pack(fill="x")

    root.mainloop()
