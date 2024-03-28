import requests
from bs4 import BeautifulSoup as bs
import time
import matplotlib


def get_price():
    URL_TEMPLATE = "https://ru.investing.com/equities/gazprom_rts"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    now_price = str(soup.find(class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'))
    now_price = now_price[-12:-6]
    return float(now_price.replace(",", "."))


i = 0
N = int(input('Введите число секунд для отслеживания котировок Газпрома\n'))
a = []
while True:
    a.append(get_price())
    time.sleep(1)
    i += 1
    print('\rЗаписаны котировки', i, 'раз из', N, end='')
    if i == N:
        break
print('\n', a)
