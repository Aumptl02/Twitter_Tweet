from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os
from os import path
import sys


PATH = os.getcwd()
DRIVER = None


def set_driver():
    global DRIVER
    driver_name = ""
    if "linux" in sys.platform:
        driver_name = "linux_geckodriver"
    elif "darwin" in sys.platform:
        driver_name = "mac_geckodriver"
    elif "win32" in sys.platform:
        driver_name = "geckodriver.exe"

    if driver_name == "":
        print("Unkown System quitting!!")
        exit(1)

    DRIVER = path.join(PATH, "drivers", driver_name)


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path=DRIVER)

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def post_tweet(self, tweet):
        bot = self.bot
        tweetbox = bot.find_element_by_xpath(
            "//a[@data-testid='SideNav_NewTweet_Button']").click()
        post = bot.find_element_by_class_name(
            'notranslate').send_keys(tweet)
        bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()

    def like_tweet(self, post_link):
        self.bot.get(post_link)
        time.sleep(10)
        like_button = self.bot.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[4]/div[3]/div/div/div/div")
        time.sleep(2)
        self.bot.execute_script("arguments[0].click();", like_button)


load_dotenv()
set_driver()

aum = TwitterBot(os.environ["USERNAME"], os.environ["PASSWORD"])
aum.login()
aum.post_tweet("BuRp")
aum.like_tweet("https://twitter.com/adnan007d/status/1398613295905460226")
