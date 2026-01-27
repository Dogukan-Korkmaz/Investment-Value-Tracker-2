from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt
from time import perf_counter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import locale
from docx import Document
from docx.shared import RGBColor


def timer_beginner():
    start_time = perf_counter()
    return start_time


def timer_ender():
    end_time = perf_counter()
    return end_time


start_time_outer = timer_beginner()

DK_INVESTMENTS = {
    "dollar": 1305,
    "euro": 2040,
    "pound": 50,
    "silver(ons)": 0,
    "quarter gold": 3,
    "1gr gold (14K)": 1.5,
    "1gr gold (22K)": 4.5,
    # 4 adet 1 gram, 1 adet 0,5gram#
    "1gr gold (24K)": 43,
    # 1 adet 5 gram, 1 adet 10 gram, 1 adet 20 gram, 7 adet 1 gram, 2 adet 0,5gram#
}

VK_INVESTMENTS = {
    "dollar": 100 + 400,
    "euro": 0,
    "quarter gold": 0,
    "1gr gold (24K)": 5,
    "turkish lira": 10000
}

SN_INVESTMENTS = {
    "euro": 300,
    "quarter gold": 0,
    "turkish lira": 455436
}


def chrome_options_maker():

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless=new")
    chrome_options.set_capability("pageLoadStrategy", "eager")
    chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--mute-audio")

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                 "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    prefs = {

        "profile.managed_default_content_settings.images": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.stylesheets": 2,
        "profile.managed_default_content_settings.fonts": 2,
        "profile.managed_default_content_settings.media": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    chrome_options.add_experimental_option("prefs", value=prefs)

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    return chrome_options


driver = webdriver.Chrome(
    options=chrome_options_maker(),
)

driver.set_window_size(960, 1080)
driver.set_window_position(0, 0)
driver.get("https://uzmanpara.milliyet.com.tr/altin-fiyatlari/")

driver2 = webdriver.Chrome(options=chrome_options_maker())
driver2.set_window_size(960, 1080)
driver2.set_window_position(960, 0)
driver2.get("https://uzmanpara.milliyet.com.tr/doviz-kurlari/")

WebDriverWait(driver, 20).until(
    ec.presence_of_element_located((By.XPATH, '/html/body/div[13]/div[7]/div[1]/div[2]/div[2]/div[1]'))
)

try:

    close_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="intclose"]'))
    )
    close_button.click()

except Exception as e:
    print(f"Reklam kapatılamadı: {e}")

price_gr_gold_14K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[17]/td[3]').text
price_gr_gold_14K = float(price_gr_gold_14K.strip(" TL").replace(".", "").replace(",", "."))
print(f"14k:{price_gr_gold_14K}")

price_gr_gold_22K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[15]/td[3]').text
price_gr_gold_22K = float(price_gr_gold_22K.strip(" TL").replace(".", "").replace(",", "."))
print(f"22k:{price_gr_gold_22K}")

price_gr_gold_24K = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[2]/td[3]').text
price_gr_gold_24K = float(price_gr_gold_24K.strip(" TL").replace(".", "").replace(",", "."))
print(price_gr_gold_24K)

price_quarter_gold = driver.find_element(By.XPATH, value='//*[@id="altinfiyat"]/tbody/tr[3]/td[3]').text
price_quarter_gold = float(price_quarter_gold.strip(" TL").replace(".", "").replace(",", "."))
print(price_quarter_gold)

price_ons_gumus = driver.find_element(By.XPATH,
                                      value="/html/body/div[13]/div[7]/div[2]/div[4]/table/tbody/tr[6]/td[3]").text
price_ons_gumus = float(price_ons_gumus.replace(".", "").replace(",", "."))
print(price_ons_gumus)

price_dollar = driver.find_element(By.XPATH, value='//*[@id="usd_header_son_data"]').text
price_dollar = float(price_dollar.replace(",", ".").replace(",", "."))
print(price_dollar)

price_euro = driver.find_element(By.XPATH, value='//*[@id="eur_header_son_data"]').text
price_euro = float(price_euro.replace(",", ".").replace(",", "."))
print(price_euro)

price_pound = driver2.find_element(By.XPATH,
                                   value="/html/body/div[13]/div[7]/div[2]/div[1]/table/tbody/tr[4]/td[3]").text
price_pound = float(price_pound.replace(",", ".").replace(",", "."))
print(price_pound)

total_dollar = DK_INVESTMENTS["dollar"] * price_dollar
total_euro = DK_INVESTMENTS["euro"] * price_euro
total_pound = DK_INVESTMENTS["pound"] * price_pound
total_gumus = DK_INVESTMENTS["silver(ons)"] * price_ons_gumus
total_quarter_gold = DK_INVESTMENTS["quarter gold"] * price_quarter_gold
total_1gr_gold_14K = DK_INVESTMENTS["1gr gold (14K)"] * price_gr_gold_14K
total_1gr_gold_22K = DK_INVESTMENTS["1gr gold (22K)"] * price_gr_gold_22K
total_1gr_gold_24K = DK_INVESTMENTS["1gr gold (24K)"] * price_gr_gold_24K

dk_total = total_dollar + total_euro + total_pound + total_1gr_gold_14K + total_quarter_gold + total_1gr_gold_22K + \
           total_1gr_gold_24K + total_gumus
print(f"Altınlar : {total_quarter_gold + total_1gr_gold_14K + total_1gr_gold_22K + total_1gr_gold_24K}")

portfoy_dolar = (total_dollar * 100) / dk_total
print(f"Dolar oranı : %{portfoy_dolar:.2f}")
portfoy_euro = (total_euro * 100) / dk_total
print(f"Euro oranı : %{portfoy_euro:.2f}")
portfoy_pound = (total_pound * 100) / dk_total
print(f"Pound oranı : %{portfoy_pound:.2f}")
portfoy_quarter_gold = (total_quarter_gold * 100) / dk_total
print(f"Çeyrek altın oranı : %{portfoy_quarter_gold:.2f}")
portfoy_gumus = (total_gumus * 100) / dk_total
print(f"Gümüş oranı : %{portfoy_gumus:.2f}")
portfoy_1gr_gold_14K = (total_1gr_gold_14K * 100) / dk_total
print(f"1gr gold (14K) oranı : %{portfoy_1gr_gold_14K:.2f}")
portfoy_1gr_gold_22K = (total_1gr_gold_22K * 100) / dk_total
print(f"1gr gold (22K) oranı : %{portfoy_1gr_gold_22K:.2f}")
portfoy_1gr_gold_24K = (total_1gr_gold_24K * 100) / dk_total
print(f"1gr gold (24K) oranı : %{portfoy_1gr_gold_24K:.2f}")

vk_total = 0
vk_total += VK_INVESTMENTS["dollar"] * price_dollar
vk_total += VK_INVESTMENTS["euro"] * price_euro
vk_total += VK_INVESTMENTS["quarter gold"] * price_quarter_gold
vk_total += VK_INVESTMENTS["1gr gold (24K)"] * price_gr_gold_24K
vk_total += VK_INVESTMENTS["turkish lira"]

sn_total = 0
sn_total += SN_INVESTMENTS["euro"] * price_euro
sn_total += SN_INVESTMENTS["quarter gold"] * price_quarter_gold
sn_total += SN_INVESTMENTS["turkish lira"]

sn_dollar = SN_INVESTMENTS["turkish lira"] / price_dollar
sn_euro = SN_INVESTMENTS["turkish lira"] / price_euro
sn_pound = SN_INVESTMENTS["turkish lira"] / price_pound
sn_gold = SN_INVESTMENTS["turkish lira"] / price_gr_gold_24K
print(f"sn_total:{sn_total}")

grand_total = dk_total+vk_total+sn_total

current_time = dt.now()
formatted_time = current_time.strftime("%d %B %Y, %H:%M:%S")

try:
    locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")
except locale.Error:
    print("tr_TR locale sistemde yüklü değil.")
    exit()


def format_info(total):
    formatted_total = locale.currency(total, grouping=True)
    return formatted_total


with open("values.txt", "a", encoding="utf-8") as file:
    file.write(
        f"\nDodo:{format_info(dk_total)}\n"
        f"Sengul:{format_info(sn_total)}\n"
        f"Vural:{format_info(vk_total)}\n"
        "--------------------------------------------------------\n"
        f"Dolar oranı : %{portfoy_dolar:.2f}\n"
        f"Euro oranı : %{portfoy_euro:.2f}\n"
        f"Pound oranı : %{portfoy_pound:.2f}\n"
        f"Gümüş oranı : %{portfoy_gumus:.2f}\n"
        f"Ceyrek altin orani : %{portfoy_quarter_gold:.2f}\n"
        f"1gr gold (14K) orani : %{portfoy_1gr_gold_14K:.2f}\n"
        f"1gr gold (22K) orani : %{portfoy_1gr_gold_22K:.2f}\n"
        f"1gr gold (24K) orani : %{portfoy_1gr_gold_24K:.2f}\n"
        "--------------------------------------------------------\n"
        f"Altin oranı : "
        f"%{(portfoy_quarter_gold + portfoy_1gr_gold_14K + portfoy_1gr_gold_22K + portfoy_1gr_gold_24K):.2f}\n"
        f"Doviz orani : %{(portfoy_dolar + portfoy_euro):.2f}\n"
        "--------------------------------------------------------\n"
        f"Bankadaki para karsiliklari:\n"
        f"Dolar:{sn_dollar:.2f}\n"
        f"Euro:{sn_euro:.2f}\n"
        f"Pound:{sn_pound:.2f}\n"
        f"Altin:{sn_gold:.2f}\n"
        "--------------------------------------------------------\n"
        f"{formatted_time}\n"
        "--------------------------------------------------------\n"
        f"Total:{format_info(grand_total)}\n"
        "**********************************************************\n"
    )
    print(f"dk_total={dk_total}\nvk_total ={vk_total}")

    def babanne_borc(filename="muazzez_borc.docx"):
        muzazzez = {
            "dollar": 500,
            "euro": 100,
            "1gr gold (24K)": 26,
            "turkish lira": 50000
        }
        muazzez_dolar = muzazzez["dollar"] * price_dollar
        muazzez_euro = muzazzez["euro"] * price_euro
        muazzez_24k_gold = muzazzez["1gr gold (24K)"] * price_gr_gold_24K
        muazzez_tl = muzazzez["turkish lira"]

        muazzez_total = muazzez_dolar + muazzez_euro + muazzez_24k_gold + muazzez_tl

        try:
            document = Document(filename)
            print("Mevcut dosya açıldı.")
        except Exception as e:
            print("Dosya yok, yeni dosya oluşturuluyor:", e)
            document = Document()

        line = document.add_paragraph()
        line.add_run("******************************************************************\n").font.color.rgb = RGBColor(
            123, 73, 98)
        line.add_run(f"{format_info(muazzez_total)}\n")
        line.add_run("------------------------------------------------------\n")
        line.add_run(f"Tarih&Saat : {formatted_time}")

        document.save(filename)
        print(f"{filename} dosyası oluşturuldu veya güncellendi. Word’de açabilirsiniz!")

    babanne_borc()


    def the_dog_move_word(origin_price, refund, filename="output.docx"):
        endgame = abs(origin_price - refund)

        if endgame < 0:
            message = f"LET'S GOOO!! KÂR: {endgame:.2f} TL"
            color = RGBColor(0, 128, 0)
        else:
            message = f"damn.. maybe next time: -{endgame:.2f} TL"
            color = RGBColor(255, 0, 0)

        try:
            document = Document(filename)
        except:
            document = Document()

        line = document.add_paragraph()
        line.add_run("******************************************************************").font.color.rgb = RGBColor(
            123, 73, 98)

        date_paragraph = document.add_paragraph()
        date_paragraph.add_run(f"Zaman: {formatted_time}\n").font.color.rgb = RGBColor(100, 100, 100)

        message_paragraph = document.add_paragraph()
        run = message_paragraph.add_run(message)
        run.font.color.rgb = color
        run.bold = True

        document.save(filename)
        print(f"{filename} dosyası oluşturuldu veya güncellendi. Word’de açabilirsiniz!")


    origin_price = 2009
    refund = int(39.29 * price_euro)

    origin_price_ebay = price_ons_gumus
    price_gumus_dolar = 132.93 * price_dollar

    the_dog_move_word(origin_price, refund)
    the_dog_move_word(price_gumus_dolar, origin_price_ebay)

    end_time_outer = timer_ender()
    the_time_value = end_time_outer - start_time_outer

    def doc_timer(time_value, filename="time_output.docx"):

        try:
            document = Document(filename)
            print("Mevcut dosya açıldı.")
        except Exception as e:
            print("Dosya yok, yeni dosya oluşturuluyor:", e)
            document = Document()

        line = document.add_paragraph()
        line.add_run("******************************************************************").font.color.rgb = RGBColor(
            123, 73, 98)

        date_paragraph = document.add_paragraph()
        date_paragraph.add_run(f"Zaman: {time_value:.2f} saniye\n").font.color.rgb = RGBColor(10, 2, 200)
        date_paragraph.add_run("------------------------------------------------------\n")
        date_paragraph.add_run(f"Tarih&Saat : {formatted_time}")

        document.save(filename)
        print(f"{filename} dosyası oluşturuldu veya güncellendi. Word’de açabilirsiniz!")


    doc_timer(the_time_value)

    driver.close()
    driver2.close()
