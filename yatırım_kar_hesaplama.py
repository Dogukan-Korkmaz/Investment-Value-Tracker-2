from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DK_INVESTMENTS = {
    "dollar": 280,
    "quarter gold": 2,
    "1gr gold (22K)": 3,
    "1gr gold (24K)": 7,
    "0,5gr gold (24K)": 2,
}

DK_TOPLAM_YATIRIM = 41279

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://uzmanpara.milliyet.com.tr/altin-fiyatlari/")

sleep(6)

try:

    close_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="intclose"]'))
    )
    close_button.click()

except Exception as e:
    print(f"Reklam kapatılamadı: {e}")


price_gr_gold_22K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[15]/td[3]').text
price_gr_gold_22K = float(price_gr_gold_22K.strip(" TL").replace(".", ""))
print(price_gr_gold_22K)

price_gr_gold_24K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[2]/td[3]').text
price_gr_gold_24K = float(price_gr_gold_24K.strip(" TL").replace(".", ""))
print(price_gr_gold_24K)

price_05_gr_gold_24K = driver.find_element(By.XPATH,
                                           value='/html/body/div[13]/div[6]/div[2]/div[3]/table/tbody/tr[4]/td[3]').text
price_05_gr_gold_24K = float(price_05_gr_gold_24K.strip(" TL").replace(".", ""))
print(price_05_gr_gold_24K)

price_quarter_gold = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[3]/td[3]').text
price_quarter_gold = float(price_quarter_gold.strip(" TL").replace(".", ""))
print(price_quarter_gold)

price_dollar = driver.find_element(By.XPATH, value='//*[@id="usd_header_son_data"]').text
price_dollar = float(price_dollar.replace(",", "."))
print(price_dollar)

dk_total = 0
dk_total += DK_INVESTMENTS["dollar"] * price_dollar
dk_total += DK_INVESTMENTS["quarter gold"] * price_quarter_gold
dk_total += DK_INVESTMENTS["1gr gold (22K)"] * price_gr_gold_22K
dk_total += DK_INVESTMENTS["1gr gold (24K)"] * price_gr_gold_24K
dk_total += DK_INVESTMENTS["0,5gr gold (24K)"] * price_05_gr_gold_24K

current_time = dt.now()
formatted_time = current_time.strftime("%d %B %Y, %H:%M:%S")

with open("degerler.txt", "a") as file:
    file.write(f"\nDodo:{dk_total}\n{formatted_time}\nTotal:{dk_total}\nOrjinal Yatırım Değeri:{DK_TOPLAM_YATIRIM}\nKAR:{dk_total - DK_TOPLAM_YATIRIM}")

print(f"dk_total={dk_total}\n")

driver.close()
