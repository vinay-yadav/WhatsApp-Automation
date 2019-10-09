from selenium import webdriver
import pickle
import time


loc = "/home/carlmark/PycharmProjects/WhatsApp_Automation/cookies.txt"
# driver = webdriver.Chrome('/home/carlmark/PycharmProjects/WhatsApp_Automation/chromedriver')
# driver.get('https://web.whatsapp.com/send?phone=919717364834')


def save_cookies(driver, location):
    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    url = "https://web.whatsapp.com" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):
    cookies = driver.get_cookies()
    for cookie in cookies:
        if domains is not None:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)

        else:
            driver.delete_all_cookies()
            return

    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)


chrome = webdriver.Chrome('/home/carlmark/PycharmProjects/WhatsApp_Automation/chromedriver')
chrome.get("https://facebook.com")
time.sleep(3)

email_box = chrome.find_element_by_id('email')
email_box.send_keys('1996yadav.vinay@gmail.com')

pass_box = chrome.find_element_by_id("pass")
pass_box.send_keys('vindroid1996')

button = chrome.find_element_by_id("u_0_b")
button.submit()

time.sleep(3)
save_cookies(chrome, loc)

chrome.get("https://www.facebook.com/yadav.vinay15")