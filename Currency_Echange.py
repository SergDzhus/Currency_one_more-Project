from tkinter import ttk
import requests
from tkinter import *
from tkinter import messagebox as mb


# генерируем список кодов валют
def generation_list_rates():
    list_currency = []
    answer = requests.get("https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    list_currency = list(json_info["rates"].keys())
    return list_currency


def func_exchange():
    code_currency = combo.get()
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

spisok_currency = generation_list_rates()

t_m = Label(text="Выберите код валюты")
t_m.pack(pady = [10, 10])

combo = ttk.Combobox(window, values=spisok_currency)
combo.pack(pady = [10, 10])

content_label = Label(window)
content_label.pack(pady = [10, 10])

bttn = Button(window, text="Получить курс рубля", command=func_exchange)
bttn.pack(pady = [10, 10])





window.mainloop()