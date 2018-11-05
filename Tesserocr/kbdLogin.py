import requests
import time
import tesserocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def check_captcha(data):
    with open('captcha.jpg', 'wb') as f:
        f.write(data)
    time.sleep(1)
    image = Image.open('captcha.jpg')
    image = image.convert('L')
    threshold = 80
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    # image.show()
    text = tesserocr.image_to_text(image)
    print("机器识别后的验证码为：" + text)
    return text


def login(username, password):
    browser = webdriver.Chrome()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    browser.get('http://passport.xxxxx.com.cn/')
    input = browser.find_element_by_id('btn_submit')
    input_username = browser.find_element_by_id('username')
    input_password = browser.find_element_by_id('password')
    input_captcha = browser.find_element_by_id('captcha')
    input_verificationcode = browser.find_element_by_id('verificationcode')

    captcha_url = input_captcha.get_attribute('src')

    input_username.send_keys(username)
    input_password.send_keys(password)
    # 读取验证码
    response = requests.get(captcha_url, headers)
    if response.status_code == 200:
        image_text = check_captcha(response.content)
        input_verificationcode.send_keys(image_text)
        input.send_keys(Keys.ENTER)


if __name__ == "__main__":
    login('xxxxx', 'yyyyyyy')
