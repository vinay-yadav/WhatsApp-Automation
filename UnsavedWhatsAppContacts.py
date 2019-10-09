from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import platform
import time


def whatsapp(chrome_driver, msg):
    book = openpyxl.load_workbook('Contacts.xlsx')
    sheet = book.active
    driver = webdriver.Chrome(f'/home/carlmark/PycharmProjects/WhatsApp_Automation/{chrome_driver}')

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
            print(f"Message delivered to {num.value}")
            time.sleep(15)

        except Exception as e:
            print(f"Message not delivered to {num.value}")

        i = i + 1

    driver.quit()


if __name__ == '__main__':
    msg = []
    init = 1
    while True:
        if init == 1:
            line = input("Message : ")
            init = init + 1
        else:
            line = input(">>>")

        if line:
            msg.append(line)
        else:
            break

    if platform.system() == 'Linux':
        chrome_driver = 'Chrome_drivers/chrome_linux'
        whatsapp(chrome_driver=chrome_driver, msg=msg)

    elif platform.system() == 'Windows':
        chrome_driver = 'Chrome_drivers/chrome_windows'
        whatsapp(chrome_driver=chrome_driver, msg=msg)