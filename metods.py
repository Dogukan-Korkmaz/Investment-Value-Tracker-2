from datetime import datetime as dt
from time import perf_counter
import locale
from docx import Document
from docx.shared import RGBColor
import requests
import requests


def get_values():
    api_url = "https://api.genelpara.com/json/"
    headers = {"User-Agent": "Mozilla/5.0"}

    params_doviz = {"list": "doviz", "sembol": "USD,EUR,GBP"}
    response_doviz = requests.get(api_url, params=params_doviz, headers=headers)
    data_doviz = response_doviz.json()

    usd_alis = float(data_doviz["data"]["USD"]["alis"])
    eur_alis = float(data_doviz["data"]["EUR"]["alis"])
    gbp_alis = float(data_doviz["data"]["GBP"]["alis"])

    params_altin = {"list": "altin", "sembol": "C,14,22,GA"}
    response_altin = requests.get(api_url, params=params_altin, headers=headers)
    data_altin = response_altin.json()

    c_alis = float(data_altin["data"]["C"]["alis"])
    altin14_alis = float(data_altin["data"]["14"]["alis"])
    altin22_alis = float(data_altin["data"]["22"]["alis"])
    ga_alis = float(data_altin["data"]["GA"]["alis"])

    print(f"USD: {usd_alis}")
    print(f"EUR: {eur_alis}")
    print(f"GBP: {gbp_alis}")
    print(f"C: {c_alis}")
    print(f"14 Ayar Altın: {altin14_alis}")
    print(f"22 Ayar Altın: {altin22_alis}")
    print(f"GA: {ga_alis}")


def timer_beginner():
    start_time = perf_counter()
    return start_time


def timer_ender():
    end_time = perf_counter()
    return end_time
