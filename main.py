import time
from threading import Thread
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


def testing(x_coor, y_coor, z, list, list1, c):
    print(list[z])
    print(list1[z])
    print(x_coor, y_coor, z, c)
    options = uc.ChromeOptions()
    service_obj = Service(f"chromedriver{c}.exe")
    options.add_argument(f'--user-data-dir=C:\\Users\\moto\\Desktop\\motoo\\profile {c}')
    # options.add_argument(f'--user-data-dir=C:\\Users\\moto\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument(fr'--profile-directory=Profile {c}')
    options.add_argument("--window-size=426,526")
    chrome = uc.Chrome(service=service_obj, options=options)

    chrome.set_window_position(x_coor, y_coor)
    chrome.get("https://mail.google.com")

    time.sleep(5)
    try:
        email = WebDriverWait(chrome, 15).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
        email.send_keys(list[z])
        time.sleep(2)
    except Exception as e:
        print("Error 2", e)

    try:
        nxt = WebDriverWait(chrome, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))
        nxt.click()
        time.sleep(10)
    except Exception as e:
        print("Error 3", e)

    try:
        password = WebDriverWait(chrome, 15).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
        password.send_keys(list1[z])
        time.sleep(2)
    except Exception as e:
        print("Error 4", e)

    try:
        nxt = WebDriverWait(chrome, 15).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]')))
        nxt.click()
        time.sleep(10)
    except Exception as e:
        print("Error 5", e)


if __name__ == '__main__':

    list = ['wetwewe503@gmail.com', 'weeewef65@gmail.com', 'fdfdgsfd03@gmail.com']
    list1 = ['khan1213', 'khan1213', 'khan1213', ]
    x = 0
    y = 0
    index = 0
    z = 0
    c = 1
    for i in range(3):
        p = Thread(target=testing, args=(x, y, z, list, list1, c))
        p.start()
        z += 1
        c += 1
        index += 1
        x = x + 530
        if index % 3 == 0:
            y = y + 400
            x = 0
    p.join()
