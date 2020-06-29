from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password, tweet):
        self.username = username
        self.password = password
        self.tweet = tweet
        self.bot = webdriver.Firefox()

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

    def post_tweet(self):
        bot = self.bot
        tweetbox = bot.find_element_by_xpath(
            "//a[@data-testid='SideNav_NewTweet_Button']").click()
        post = bot.find_element_by_class_name(
            'notranslate').send_keys(self.tweet)
        bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()


aum = TwitterBot("Enter Your Username here", "Enter Your Password Here",
                 "Enter Your Tweet Here.")
aum.login()
aum.post_tweet()
