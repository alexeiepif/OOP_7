#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

    frame = tk.Frame()
    frame.pack()

    for color in colors:
        tk.Button(
            frame,
            text="",
            bg=colors[color],
            command=partial(calc, color, entry, lable),
            width=5,
            height=2,
        ).pack(side="left", padx=2, pady=2)

    root.mainloop()
