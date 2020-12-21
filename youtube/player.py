import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .links import Search

def Play(query):
    link=Search(str(query))
    driver=webdriver.Chrome('src/chromedriver')
    driver.get(link)
    while True:
        try:
            full_screen=driver.find_element_by_xpath('//*[@id="movie_player"]/div[32]/div[2]/div[2]/button[9]')
            full_screen.send_keys(Keys.RETURN)
            break
        except:
            pass
        
    while True:
        try:
            play_btn=driver.find_element_by_xpath('//*[@id="movie_player"]/div[5]/button')
            play_btn.send_keys(Keys.RETURN)
            break
        except:
            pass
    