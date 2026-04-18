from selenium.webdriver import Keys

PROMISED_DOWN = 100
PROMISED_UP = 10
TWITTER_EMAIL = "akstolearnhere@gmail.com"
TWITTER_PASSWORD = "aksTolearnhere123@"
TWITTER_URL = "https://x.com/login"
TWITTER_EMAIL_CLASS = "r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"
TWITTER_PASSWORD_CLASS = "r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"
TWEET = "Hey Internet Provider why is my internet speed is at download speed of {self.down} and upload speed of {self.up}"

INTERNET_SPEED_TEST_URL = "https://www.speedtest.net/"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # Disables the blink features that reveal automation
        self.chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        print("Going to check internet speed")
        self.driver.get(INTERNET_SPEED_TEST_URL)
        go_button = self.driver.find_element(By.CLASS_NAME,"start-text")
        go_button.click()
        WebDriverWait(self.driver, 60).until(EC.url_contains("result"))
        self.down = self.driver.find_element(By.XPATH,"//span[contains(@class,'download-speed')]")
        print(f"download speed in mbps:{self.down.text}")
        self.up = self.driver.find_element(By.XPATH, "//span[contains(@class,'upload-speed')]")
        print(f"upload speed in mbps:{self.up.text}")


    def tweet_at_provider(self):
        print("Tweeting on twitter/x")
        self.driver.get(TWITTER_URL)
        WebDriverWait(self.driver, 60)
        google_span = self.driver.find_element(By.CLASS_NAME,"nsm7Bb-HzV7m-LgbsSe-BPrWId")
        print( TWITTER_EMAIL)
        google_span.click()
        email_input = self.driver.find_element(By.ID,"identifierId")
        email_input.send_keys(TWITTER_EMAIL,Keys.ENTER)
        WebDriverWait(self.driver,100)
        password = self.driver.find_element(By.XPATH, "//input[@contains,'whsOnd']")
        password.clear()
        password.send_keys(TWITTER_PASSWORD)






bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
#bot.tweet_at_provider()



