from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(limit)

user = input("Enter your username: ")
pwd = input("Enter your password: ")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.get("https://www.instagram.com")
    sleep_for_period_of_time()

    username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(user)
    password_input.send_keys(pwd)
    sleep_for_period_of_time()

    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep_for_period_of_time()

    hashtag = input("Enter your hashtag name: ")
    browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
    sleep_for_period_of_time()

    first_pic = browser.find_element(By.XPATH, "//div[@class='_aaq8']/div/div/div[1]/div[1]/a")
    first_pic.click()

    num_post = input("How many post you want to like and leave a comment: ")
    cmmt = input("Type your comment: ")
    sleep_for_period_of_time()

    for i in range(int(num_post)):

        # Like a post 
        like_post = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_8-yf5')]/span[@class='_15y0l']")))
        like_post.click()
        print("Liked!")
        sleep_for_period_of_time()

        #Comment on a post
        cmmt_post = browser.find_element(By.XPATH, "//textarea[@class='_2-a2iV _29SDf']")
        cmmt_post.click()
        cmmt_post = browser.find_element(By.XPATH,

    else:
        pass
        
        #Move on to the next Post
        next_post = browser.find_element(By.XPATH, "//button[@class='_abl-']//*[name()='svg' and @aria-label='Next']")
        next_post.click()
        print("post " + str(i) + " done!")
        print("Next!")
        sleep_for_period_of_time()

    #Quit the Program
    answer = input("The programm finished! Click on 'e' to exit.. ")
    if answer.lower().startswith("e"):
        browser.quit()
        exit()

if __name__ == "__main__":
    main()
