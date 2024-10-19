import requests
from tkinter import *
from tkinter import messagebox as mb


def func_exchange():
    code_currency = e.get().upper()
    if code_currency:
        answer = requests.get("https://open.er-api.com/v6/latest/RUB")
        json_info = answer.json()
        if code_currency in json_info["rates"]:
            rezult = json_info["rates"][code_currency]
            content_label.config(text=f"1 RUB - {rezult}{code_currency}")
            content_label.config(fg="green")
        else:
            content_label.config(text=f"Такого кода валюты не существует!")
            content_label.config(fg="red")
    else:
        content_label.config(text=f"Код валюты не введен!")
        content_label.config(fg="red")


window = Tk()
window.title("Курс валют")
window.geometry("400x500")

e = Entry(window)
e.pack()

content_label = Label(window)
content_label.pack()

bttn = Button(window, text="Получить курс рубля", command=func_exchange)
bttn.pack()





window.mainloop()