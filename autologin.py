import time
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def testing(x_coor, y_coor, z, c):
    print(x_coor, y_coor, z, c)
    options = webdriver.ChromeOptions()
    service_obj = Service(f"chromedriver{c}.exe")
    options.add_argument(f'--user-data-dir=C:\\Users\\moto\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument(fr'--profile-directory=Profile {c}')
    options.add_argument("--window-size=326,526")
    chrome = webdriver.Chrome(service=service_obj, options=options)
    chrome.set_window_position(x_coor, y_coor)
    chrome.get("https://mail.google.com")
    # chrome.get("https://www.youtube.com/")
    time.sleep(20)


if __name__ == '__main__':

    x = 0
    y = 0
    index = 0
    z = 0
    c = 1
    for i in range(3):
        time.sleep(4)
        p = Thread(target=testing, args=(x, y, z, c))
        p.start()
        z += 1
        c += 1
        index += 1
        x = x + 500
        if index % 3 == 0:
            y = y + 400
            x = 0
    p.join()
