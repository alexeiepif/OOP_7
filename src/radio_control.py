#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: виджеты Radiobatton и Checkbutton поддерживают большинство
# свойств оформления внешнего вида, которые есть у других элементов
# графического интерфейса. При этом у Radiobutton есть особое свойство indicatoron.
# По умолчанию он равен единице, в этом случае радиокнопка выглядит как нормальная
# радиокнопка. Однако если присвоить этой опции ноль, то виджет Radiobutton
# становится похожим на обычную кнопку по внешнему виду. Но не по смыслу.
# Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
# индикатор которых выключен (indicatoron=0). Если какая-нибудь кнопка включается,
# то в метке должна отображаться соответствующая ей информация. Обычных кнопок
# в окне быть не должно.

import tkinter as tk
from functools import partial


def calc(value: int, lable: tk.Label) -> None:
    match value:
        case 1:
            txt = "Первый radiobutton"
        case 2:
            txt = "Второй radiobutton"
        case 3:
            txt = "Третий radiobutton"
    lable.config(text=txt)


if __name__ == "__main__":
    root = tk.Tk()
    fr = tk.Frame(root)
    fr.pack(side="left")
    var = tk.IntVar()
    var.set(1)
    rd1 = tk.Radiobutton(
        fr, text="1", value=1, width=10, height=5, indicatoron=False, variable=var
    )
    rd1.pack()
    rd2 = tk.Radiobutton(
        fr, text="2", value=2, width=10, height=5, indicatoron=False, variable=var
    )
    rd2.pack()
    rd3 = tk.Radiobutton(
        fr, text="3", value=3, width=10, height=5, indicatoron=False, variable=var
    )
    rd3.pack()
    lable = tk.Label(root, text="Первый radiobutton")
    lable.pack(side="left", anchor="center", fill="y", padx=30)

    for rd in [rd1, rd2, rd3]:
        rd.config(command=partial(calc, rd["value"], lable))

    root.mainloop()
