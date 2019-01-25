
import time
import random
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def autoSelect():
    driver.get('https://www.wjx.cn/m/27168497.aspx')

    xpath1 = '//*[@id="div1"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_1 = driver.find_elements_by_xpath(xpath1)[0]
    answer_1.click()

    xpath2 = '//*[@id="div2"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_2 = driver.find_elements_by_xpath(xpath2)[0]
    answer_2.click()

    xpath3 = '//*[@id="div3"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_3 = driver.find_elements_by_xpath(xpath3)[0]
    answer_3.click()

    xpath4 = '//*[@id="div4"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_4 = driver.find_elements_by_xpath(xpath4)[0]
    answer_4.click()

    xpath5 = '//*[@id="div5"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_5 = driver.find_elements_by_xpath(xpath5)[0]
    answer_5.click()

    ### 多选题。
    qList_6 = [str(x) for x in range(1, 6)]
    aList_6 = random.sample(qList_6, 3)
    for i in aList_6:
        xpath6 = '//*[@id="div6"]/div[2]/div[%s]' % i
        answer_6 = driver.find_elements_by_xpath(xpath6)[0]
        answer_6.click()

    qList_7 = [str(x) for x in range(1, 8)]
    aList_7 = random.sample(qList_7, 3)
    for i in aList_7:
        xpath7 = '//*[@id="div7"]/div[2]/div[%s]' % i
        answer_7 = driver.find_elements_by_xpath(xpath7)[0]
        answer_7.click()

    qList_8 = [str(x) for x in range(1, 7)]
    aList_8 = random.sample(qList_8, 3)
    for i in aList_8:
        xpath8 = '//*[@id="div8"]/div[2]/div[%s]' % i
        answer_8 = driver.find_elements_by_xpath(xpath8)[0]
        answer_8.click()

    xpath9 = '//*[@id="div9"]/div[2]/div[%s]' % str(random.randint(1, 5))
    answer_9 = driver.find_elements_by_xpath(xpath9)[0]
    answer_9.click()

    xpath10 = '//*[@id="div10"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_10 = driver.find_elements_by_xpath(xpath10)[0]
    answer_10.click()

    xpath11 = '//*[@id="div11"]/div[2]/div[%s]' % str(random.randint(1, 5))
    answer_11 = driver.find_elements_by_xpath(xpath11)[0]
    answer_11.click()

    xpath12 = '//*[@id="div12"]/div[2]/div[%s]' % str(random.randint(1, 4))
    answer_12 = driver.find_elements_by_xpath(xpath12)[0]
    answer_12.click()

    # 判断页面是否有验证码
    captcha = ifcaptcha()
    if captcha:
        captchaCode()
        code = identify()
        print('验证码：%s' % code)
        inpu = driver.find_elements_by_css_selector('#yucinput')[0]
        inpu.send_keys(code)


    submit = driver.find_elements_by_css_selector('#ctlNext')[0]
    submit.click()

    try:
        finished = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tbAward > tbody > tr:nth-child(2) > td:nth-child(2) > a"))
        )
        print('————————第%d页已完成————————' % index)
    except:
        print('————————第%d页失败！————————' % index)

def ifcaptcha():
    # 判断页面是否出现验证码，存在返回True。
    captcha_submit = driver.find_elements_by_css_selector('#tdCode')[0]
    if captcha_submit.get_attribute('style')[9:14] == 'block':
        return True
    else:
        return False

def captchaCode():
    inpu = driver.find_elements_by_css_selector('#yucinput')[0]
    inpu.click()
    time.sleep(0.5)
    img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#imgCode"))
    )
    # 截取整个网页
    driver.save_screenshot('wholeWeb.png')
    # 定位验证码位置
    left =img.location['x']
    top = img.location['y']
    right = img.location['x'] + img.size['width']
    bottom = img.location['y'] + img.size['height']

    im = Image.open('wholeWeb.png')
    im = im.crop((left, top, right, bottom))
    im.save('captcha.png')

def identify():
    '''
    验证码识别
    :return: 验证码
    '''
    chaojiying = Chaojiying_Client('超级鹰账号', '超级鹰密码', '软件key')
    im = open('captcha.png', 'rb').read()
    return chaojiying.PostPic(im, 1902)['pic_str']


if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    for index in range(1,51):
        autoSelect()
