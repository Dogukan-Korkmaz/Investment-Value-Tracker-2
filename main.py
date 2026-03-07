from datetime import datetime as dt
import locale
from docx import Document
from docx.shared import RGBColor
from metods import timer_beginner, timer_ender
from portfolios import DK_INVESTMENTS, VK_INVESTMENTS, SN_INVESTMENTS

start_time_outer = timer_beginner()




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
            "euro": 100-100,
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
