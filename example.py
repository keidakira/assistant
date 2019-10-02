import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
while True:
    i = input("Keida: What's up?\n")
    sngs = "light me up!|play my songs|play something|up my mood"
    vid = "download video"
    qu = "bye|quit|tata|night|bubyee"
    booking = "book|flights|book flights"
    if i.lower() in sngs:
        os.system("bot.vbs")
        break
    if i.lower() in vid:
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        url = "https://www.youtube.com/results?search_query="
        driver = webdriver.Firefox()
        x = input("What video do you want? ")
        driver.get(url+x)
        e = driver.find_element_by_css_selector("#contents > ytd-video-renderer a")
        abcd = e.get_attribute("href")
        driver.quit()
        driver = webdriver.Firefox()
        driver.get("https://en.savefrom.net/")
        e = driver.find_element_by_id("sf_url")
        e.send_keys(abcd, Keys.ENTER)
        driver.implicitly_wait(15)
        ex = driver.find_element_by_css_selector(".link-download")
        link = ex.get_attribute("href")
        driver.quit()
        driver = webdriver.Firefox()
        driver.get(link)
        driver.quit()
    if i.lower() in booking:
        url = "https://www.world-airport-codes.com/search/?s=rajiv"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        ht = urlopen(req)
        soup = BeautifulSoup(ht, "lxml")
        f = open("index.html", "w")
        for i in soup:
            f.write(str(i))
        f.close()
    if i.lower() in qu:
        print("Have a good day, boss :)")
        exit(0)
    else:
        print("Sorry, I couldn't understand you. Could you repeat?")
