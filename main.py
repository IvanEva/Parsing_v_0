import requests
from bs4 import BeautifulSoup as bs
import time
import matplotlib.pyplot as plt


def get_price_Gasprom():  # Функция для запроса данных
    URL_TEMPLATE = "https://ru.investing.com/equities/gazprom_rts"
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    now_price = str(soup.find(class_='text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'))
    now_price = now_price[-12:-6]
    return float(now_price.replace(",", "."))


def print_progress(past_t_, N_):  # Функция для вывода прогресса и времени работы программы
    dl = 30
    proc = past_t_ / (N_ * 60)
    prog = int(past_t_ * dl / (N_ * 60))
    print('\rПрошло времени: %.2f (сек) из %.2f (сек)' % (past_t, float(N * 60)),
          '||' + '#' * prog + '-' * (dl - prog) + '||', '%.1f %% выполнено' % (proc*100), end='')


i = 0
N = int(input('Введите время для отслеживания котировок Газпрома (в минутах): '))
a = []  # Массив для хранения данных о цене
b = []  # Массив для хранения времени (в секундах) получения этих данных от начала цикла
start_t = time.time()
now_t = start_t
finish_t = start_t + N * 60
while now_t < finish_t:
    past_t = N * 60 - (finish_t - now_t)
    a.append(get_price_Gasprom())
    b.append(past_t)
    print_progress(past_t, N)
    now_t = time.time()
    i += 1
    time.sleep(3)
print_progress(N*60, N)
plt.plot(b, a)
plt.axes((0, N*60, min(a), max(a)))
plt.show()
