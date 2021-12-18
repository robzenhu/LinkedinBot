from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LinkedinBot:
    def __init__(self,username , password):
        self.username =username
        self.password = password
        self.driver= webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get('https://www.linkedin.com/login/')
        time.sleep(2)
        user = driver.find_element_by_xpath('//*[@id="username"]')
        user.send_keys(self.username)
        passw = driver.find_element_by_xpath('//*[@id="password"]')
        passw.send_keys(self.password)
        passw.send_keys(Keys.RETURN)
        time.sleep(2)
        for i in range(1,6):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
              
        all_buttons = driver.find_elements_by_tag_name('button')
        like_btn =[btn for btn in all_buttons if btn.text == 'Gostei']
        for btn in like_btn:
            btn.click()
            time.sleep(2)

          

bot = LinkedinBot('Seu Usuario','Sua Senha')
bot.login()

