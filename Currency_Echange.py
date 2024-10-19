from tkinter import ttk
import requests
from tkinter import *
# from tkinter import messagebox as mb


# генерируем список кодов валют
#def generation_list_rates():
#    answer = requests.get("https://open.er-api.com/v6/latest/RUB")
#    json_info = answer.json()
#    list_currency = list(json_info["rates"].keys())
#    return list_currency
def update_base_label1(event):
    code = combo_from_1.get()
    name = spisok_currency[code]
    base_label1.config(text=name)


def update_base_label2(event):
    code = combo_from_2.get()
    name = spisok_currency[code]
    base_label2.config(text=name)


def update_target_label(event):
    code = combo_to.get()
    name = spisok_currency[code]
    label_to.config(text=name)

def func_exchange_1():
    code_currency_target = combo_to.get()
    code_currency_base_1 = combo_from_1.get()
    if code_currency_target and code_currency_base_1:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_currency_base_1}")
        answer.raise_for_status()
        json_info = answer.json()
        if code_currency_target in json_info["rates"]:
            rezult = json_info["rates"][code_currency_target]
            content_label_1.config(text=f"1 {code_currency_base_1} - {rezult:.2f}{code_currency_target}")
            content_label_1.config(fg="green")
        else:
            content_label_1.config(text=f"Такого кода валюты не существует!")
            content_label_1.config(fg="red")
    else:
        content_label_1.config(text=f"Код валюты не введен!")
        content_label_1.config(fg="red")


def func_exchange_2():
    code_currency_target = combo_to.get()
    code_currency_base_2 = combo_from_2.get()
    if code_currency_target and code_currency_base_2:
        answer = requests.get(f"https://open.er-api.com/v6/latest/{code_currency_base_2}")
        answer.raise_for_status()
        json_info = answer.json()
        if code_currency_target in json_info["rates"]:
            rezult = json_info["rates"][code_currency_target]
            content_label_2.config(text=f"1 {code_currency_base_2} - {rezult:.2f}{code_currency_target}")
            content_label_2.config(fg="green")
        else:
            content_label_2.config(text=f"Такого кода валюты не существует!")
            content_label_2.config(fg="red")
    else:
        content_label_2.config(text=f"Код валюты не введен!")
        content_label_2.config(fg="red")


def func_exchange():
    func_exchange_1()
    func_exchange_2()


window = Tk()
window.title("Курс валют")
window.geometry("400x500")

spisok_currency = {
    "RUB": "Российский рубль",
    "USD": "Доллар США",
    "GBP": "Британский фунт стерлингов",
    "AED": "Дирхам ОАЭ",
    "AFN": "Афгани",
    "ALL": "Албанский лек",
    "AMD": "Армянский драм",
    "ANG": "Нидерландский антильский гульден",
    "AOA": "Ангольская кванза",
    "ARS": "Аргентинское песо",
    "AUD": "Австралийский доллар",
    "AWG": "Арубанский флорин",
    "AZN": "Азербайджанский манат",
    "BAM": "Конвертируемая марка Боснии и Герцеговины",
    "BBD": "Барбадосский доллар",
    "BDT": "Бангладешская така",
    "BGN": "Болгарский лев",
    "BHD": "Бахрейнский динар",
    "BIF": "Бурундийский франк",
    "BMD": "Бермудский доллар",
    "BND": "Брунейский доллар",
    "BOB": "Боливийский боливиано",
    "BRL": "Бразильский реал",
    "BSD": "Багамский доллар",
    "BTN": "Бутанский нгултрум",
    "BWP": "Ботсванская пула",
    "BYN": "Белорусский рубль",
    "BZD": "Белизский доллар",
    "CAD": "Канадский доллар",
    "CDF": "Конголезский франк",
    "CHF": "Швейцарский франк",
    "CLP": "Чилийское песо",
    "CNY": "Китайский юань",
    "COP": "Колумбийское песо",
    "CRC": "Костариканский колон",
    "CUP": "Кубинское песо",
    "CVE": "Эскудо Кабо-Верде",
    "CZK": "Чешская крона",
    "DJF": "Франк Джибути",
    "DKK": "Датская крона",
    "DOP": "Доминиканское песо",
    "DZD": "Алжирский динар",
    "EGP": "Египетский фунт",
    "ERN": "Эритрейская накфа",
    "ETB": "Эфиопский быр",
    "EUR": "Евро",
    "FJD": "Доллар Фиджи",
    "FKP": "Фунт Фолклендских островов",
    "FOK": "Фарерская крона",
    "GEL": "Грузинский лари",
    "GGP": "Фунт Гернси",
    "GHS": "Ганский седи",
    "GIP": "Гибралтарский фунт",
    "GMD": "Гамбийский даласи",
    "GNF": "Гвинейский франк",
    "GTQ": "Гватемальский кетсаль",
    "GYD": "Гайанский доллар",
    "HKD": "Гонконгский доллар",
    "HNL": "Гондурасская лемпира",
    "HRK": "Хорватская куна",
    "HTG": "Гаитянский гурд",
    "HUF": "Венгерский форинт",
    "IDR": "Индонезийская рупия",
    "ILS": "Израильский шекель",
    "IMP": "Фунт Острова Мэн",
    "INR": "Индийская рупия",
    "IQD": "Иракский динар",
    "IRR": "Иранский риал",
    "ISK": "Исландская крона",
    "JEP": "Фунт Джерси",
    "JMD": "Ямайский доллар",
    "JOD": "Иорданский динар",
    "JPY": "Японская иена",
    "KES": "Кенийский шиллинг",
    "KGS": "Киргизский сом",
    "KHR": "Камбоджийский риель",
    "KID": "Доллар Кирибати",
    "KMF": "Франк Комор",
    "KRW": "Южнокорейская вона",
    "KWD": "Кувейтский динар",
    "KYD": "Доллар Каймановых островов",
    "KZT": "Казахстанский тенге",
    "LAK": "Лаосский кип",
    "LBP": "Ливанский фунт",
    "LKR": "Шри-ланкийская рупия",
    "LRD": "Либерийский доллар",
    "LSL": "Лоти Лесото",
    "LYD": "Ливийский динар",
    "MAD": "Марокканский дирхам",
    "MDL": "Молдавский лей",
    "MGA": "Малагасийский ариари",
    "MKD": "Северомакедонский динар",
    "MMK": "Мьянманский кьят",
    "MNT": "Монгольский тугрик",
    "MOP": "Патака Макао",
    "MRU": "Мавританская угия",
    "MUR": "Маврикийская рупия",
    "MVR": "Мальдивская руфия",
    "MWK": "Малавийская квача",
    "MXN": "Мексиканское песо",
    "MYR": "Малайзийский ринггит",
    "MZN": "Мозамбикский метикал",
    "NAD": "Намибийский доллар",
    "NGN": "Нигерийская найра",
    "NIO": "Никарагуанская кордоба",
    "NOK": "Норвежская крона",
    "NPR": "Непальская рупия",
    "NZD": "Новозеландский доллар",
    "OMR": "Оманский риал",
    "PAB": "Панамский бальбоа",
    "PEN": "Перуанский соль",
    "PGK": "Кина Папуа-Новой Гвинеи",
    "PHP": "Филиппинское песо",
    "PKR": "Пакистанская рупия",
    "PLN": "Польский злотый",
    "PYG": "Парагвайский гуарани",
    "QAR": "Катарский риал",
    "RON": "Румынский лей",
    "RSD": "Сербский динар",
    "RWF": "Франк Руанды",
    "SAR": "Саудовский риал",
    "SBD": "Доллар Соломоновых островов",
    "SCR": "Сейшельская рупия",
    "SDG": "Суданский фунт",
    "SEK": "Шведская крона",
    "SGD": "Сингапурский доллар",
    "SHP": "Фунт Святой Елены",
    "SLE": "Леоне Сьерра-Леоне",
    "SLL": "Сьерра-леонский леоне",
    "SOS": "Сомалийский шиллинг",
    "SRD": "Суринамский доллар",
    "SSP": "Южносуданский фунт",
    "STN": "Добра Сан-Томе и Принсипи",
    "SYP": "Сирийский фунт",
    "SZL": "Свазилендский лилангени",
    "THB": "Тайский бат",
    "TJS": "Таджикский сомони",
    "TMT": "Туркменский манат",
    "TND": "Тунисский динар",
    "TOP": "Паанга Тонга",
    "TRY": "Турецкая лира",
    "TTD": "Доллар Тринидада и Тобаго",
    "TVD": "Доллар Тувалу",
    "TWD": "Тайваньский доллар",
    "TZS": "Танзанийский шиллинг",
    "UAH": "Украинская гривна",
    "UGX": "Угандийский шиллинг",
    "UYU": "Уругвайское песо",
    "UZS": "Узбекский сум",
    "VES": "Венесуэльский боливар",
    "VND": "Вьетнамский донг",
    "VUV": "Вату Вануату",
    "WST": "Тала Самоа",
    "XAF": "Франк КФА BEAC",
    "XCD": "Восточно-карибский доллар",
    "XDR": "СПЗ (Специальные права заимствования)",
    "XOF": "Франк КФА BCEAO",
    "XPF": "Французский тихоокеанский франк",
    "YER": "Йеменский риал",
    "ZAR": "Южноафриканский рэнд",
    "ZMW": "Замбийская квача",
    "ZWL": "Зимбабвийский доллар"
}

t_m_from_1 = Label(text="Выберите код первой базовой валюты")
t_m_from_1.pack(padx = 10, pady = 10)
combo_from_1 = ttk.Combobox(window, state="readonly", values=list(spisok_currency.keys()))
combo_from_1.pack(padx = 10, pady = 10)
combo_from_1.bind("<<ComboboxSelected>>", update_base_label1)
base_label1 = ttk.Label()
base_label1.pack(padx=10, pady=10)

t_m_from_2 = Label(text="Выберите код второй базовой валюты")
t_m_from_2.pack(padx = 10, pady = 10)
combo_from_2 = ttk.Combobox(window, state="readonly", values=list(spisok_currency.keys()))
combo_from_2.pack(padx = 10, pady = 10)
combo_from_2.bind("<<ComboboxSelected>>", update_base_label2)
base_label2 = ttk.Label()
base_label2.pack(padx=10, pady=10)

t_m_to = Label(text="Выберите код конечной валюты")
t_m_to.pack(padx = 10, pady = 10)
combo_to = ttk.Combobox(window, state="readonly", values=list(spisok_currency.keys()))
combo_to.pack(padx = 10, pady = 10)
combo_to.bind("<<ComboboxSelected>>", update_target_label)
label_to = ttk.Label()
label_to.pack(padx=10, pady=10)

content_label_1 = Label(window)
content_label_1.pack(padx = 10, pady = 10)

content_label_2 = Label(window)
content_label_2.pack(padx = 10, pady = 10)

bttn = Button(window, text="Получить курс", command=func_exchange)
bttn.pack(padx = 10, pady = 10)

window.mainloop()