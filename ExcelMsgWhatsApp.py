from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import platform
import time


def whatsapp(chrome_driver):
    book = openpyxl.load_workbook('Contacts.xlsx')
    sheet = book.active
    driver = webdriver.Chrome(f'/home/carlmark/PycharmProjects/WhatsApp_Automation/{chrome_driver}')
    msg = sheet["C2"].value
    msg = msg.split('\n')

    i = 2
    while True:
        num = sheet[f"A{i}"]
        if num.value is None:
            break

        try:
            if i == 2:
                driver.get("https://web.whatsapp.com/")
                input("Press Enter after scanning the QR Code")

            driver.get(f"https://web.whatsapp.com/send?phone=91{num.value}")
            time.sleep(15)
            msg_box = driver.find_element_by_class_name("_13mgZ")
            for j in range(len(msg)):
                msg_box.send_keys(msg[j])
                time.sleep(1)
                msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
            button = driver.find_element_by_class_name("_3M-N-")
            time.sleep(2)
            button.click()
            print(i-1, f"Complete {num.value}")
            time.sleep(20)
            sheet[f"B{i}"] = 'Complete'

        except Exception as e:
            print(i-1, f"Incomplete {num.value}")
            sheet[f"B{i}"] = 'Incomplete'

        book.save('Contacts.xlsx')
        i = i + 1

    driver.quit()


if __name__ == '__main__':
    if platform.system() == 'Linux':
        chrome_driver = 'Chrome_drivers/chrome_linux'
        whatsapp(chrome_driver=chrome_driver)

    elif platform.system() == 'Windows':
        chrome_driver = 'Chrome_drivers/chrome_windows'
        whatsapp(chrome_driver=chrome_driver)