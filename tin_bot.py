from selenium import webdriver
import time 
import random
class TinderBot():
    def login(self):
        self.driver.get("http://www.tinder.com")
        time.sleep(2)
        try:
            accpt_cookies=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            accpt_cookies.click()
            print("cookies_accpted")
        finally:
            pass
        try:
            time.sleep(5)
            login_more_option=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
            login_more_option.click()
            time.sleep(5)
            print("more option butten clicked")
        except Exception:
            pass
        
        fb_button=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        #                                            //*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button
        fb_button.click()
        print("fb logedin")
        time.sleep(3)
        base_window=self.driver.window_handles[0]
        #facebook login
        popup=self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(4)
        email_in=self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('Facebook_userid')
        time.sleep(2)
        fb_pass=self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pass.send_keys('Facebook_password')
        time.sleep(2)
        fb_login_btn=self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login_btn.click()
        time.sleep(10)
        #fb_login_btn.click()
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(3)
        location_allow=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        location_allow.click()
        time.sleep(10)
        notify_no_enable=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        notify_no_enable.click()
        time.sleep(10)
        set_no_loctaion=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span')
        set_no_loctaion.click()
        time.sleep(10)
        #after_fb_login()
        #like_profile=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button/span/svg')
        while True:
            print("into ittration ")
            like_profile=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
            like_profile.click()
            time.sleep(3)
            try:
                if_match=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/a')
                if_match.click()
            except Exception:
                pass
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.login()
	#def after_fb_login(self):
bot=TinderBot()
#//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button