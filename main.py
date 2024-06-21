from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DK_INVESTMENTS = {
    "euro": 620,
    "quarter gold": 1,
    "1gr gold (22K)": 2,
    "1gr gold (24K)": 3
}

VK_INVESTMENTS = {
    "dollar": 500,
    "euro": 400,
    "quarter gold": 3
}

sleep(3)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://uzmanpara.milliyet.com.tr/altin-fiyatlari/")

try:

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="intclose"]'))
    )
    close_button.click()

except Exception as e:
    print(f"Reklam kapatılamadı: {e}")

price_gr_gold_22K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[15]/td[3]').text
price_gr_gold_22K = float(price_gr_gold_22K.strip(" TL").replace(".", ""))
price_gr_gold_24K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[2]/td[3]').text
price_gr_gold_24K = float(price_gr_gold_24K.strip(" TL").replace(".", ""))
price_quarter_gold = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[3]/td[3]').text
price_quarter_gold = float(price_quarter_gold .strip(" TL").replace(".", ""))
price_dollar = driver.find_element(By.XPATH, value='//*[@id="usd_header_son_data"]').text
price_dollar = float(price_dollar.replace(",", "."))
price_euro = driver.find_element(By.XPATH, value='//*[@id="eur_header_son_data"]').text
price_euro = float(price_euro.replace(",", "."))

dk_total = 0
dk_total += DK_INVESTMENTS["euro"] * price_euro
dk_total += DK_INVESTMENTS["quarter gold"] * price_quarter_gold
dk_total += DK_INVESTMENTS["1gr gold (22K)"] * price_gr_gold_22K
dk_total += DK_INVESTMENTS["1gr gold (24K)"] * price_gr_gold_24K

vk_total = 0
vk_total += VK_INVESTMENTS["dollar"] * price_dollar
vk_total += VK_INVESTMENTS["euro"] * price_euro
vk_total += VK_INVESTMENTS["quarter gold"] * price_quarter_gold

current_time = dt.now()
formatted_time = current_time.strftime("%d %B %Y, %H:%M:%S")

with open("values.txt", "a") as file:
    file.write(f"\nDodo:{dk_total}\nVural:{vk_total}\n{formatted_time}\nTotal:{dk_total + vk_total}\n")

print(f"dk_total={dk_total}\nvk_total ={vk_total}")

driver.close()
