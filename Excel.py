# import pandas as pd
#
# data = pd.read_excel('Vijay Vihar.xlsx')
# df = pd.DataFrame(data, columns=['Property ID'])
# print(type(df))
# print(df)

import openpyxl
from selenium import webdriver
import time

driver = webdriver.Chrome('/home/carlmark/PycharmProjects/WhatsApp_Automation/chromedriver')
driver.get('https://web.whatsapp.com/')

input('Press Enter after scanning the QR Code')

# reading excel
book = openpyxl.load_workbook('Contacts.xlsx')
sheet = book.active

for i in range(2, 6):
    name = sheet[f'A{i}']
    print(name.value)

    try:
        # name = ['Sonu Mama', 'Mom', 'Tanya', 'Nicky Bro']
        msg = 'Hello'

    # for i in range(len(name)):
        chat = driver.find_element_by_xpath("//div[@title = 'New chat']")
        chat.click()

        search = driver.find_element_by_class_name('eiCXe')
        search.send_keys(name.value)
        time.sleep(1)
        user = driver.find_element_by_xpath(f"//span[@title = '{name.value}']")
        user.click()

        msg_box = driver.find_element_by_class_name("_13mgZ")

        count = 1
        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name("_3M-N-")
            time.sleep(5)
            button.click()
            time.sleep(20)

    except Exception as e:
        print(e)
