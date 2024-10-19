from tkinter import ttk
import requests
from tkinter import *
from tkinter import messagebox as mb


# генерируем список кодов валют
def generation_list_rates():
    answer = requests.get("https://open.er-api.com/v6/latest/RUB")
    json_info = answer.json()
    list_currency = list(json_info["rates"].keys())
    print(list_currency)
    return list_currency


def func_exchange():
    code_currency_target = combo_to.get()
    code_currency_base = combo_from.get()
    if code_currency_target and code_currency_base:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_currency_base}")
        json_info = answer.json()
        if code_currency_target in json_info["rates"]:
            rezult = json_info["rates"][code_currency_target]
            content_label.config(text=f"1 {code_currency_base} - {rezult}{code_currency_target}")
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

t_m_from = Label(text="Выберите код базовой валюты")
t_m_from.pack(pady = [10, 10])

combo_from = ttk.Combobox(window, values=spisok_currency)
combo_from.pack(pady = [10, 10])

t_m_to = Label(text="Выберите код конечной валюты")
t_m_to.pack(pady = [10, 10])

combo_to = ttk.Combobox(window, values=spisok_currency)
combo_to.pack(pady = [10, 10])

content_label = Label(window)
content_label.pack(pady = [10, 10])

bttn = Button(window, text="Получить курс", command=func_exchange)
bttn.pack(pady = [10, 10])





window.mainloop()