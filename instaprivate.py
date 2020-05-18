from selenium import webdriver
from PIL import Image
import  time
import urllib.request
driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver")
driver.get("url of that account")
driver.maximize_window()
input("enter the key")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/div[1]/div/button").click()
lst_height=driver.execute_script("document.body.scrollHeight")
i=0
while(i<1):
    i+=1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
posts=[]
links=driver.find_elements_by_tag_name('a')
print(links)
for link in links:
    post=link.get_attribute("href")
    if ('/p/') in post:
        posts.append(post)
print(posts)
download_url=''
k=0
for post in posts:
    driver.get(post)
    driver.execute_script("window.scrollBy(0,35)","")
    time.sleep(5)
    driver.save_screenshot("E:\picss\{}.png".format(k))
    im = Image.open(r"E:\picss\{}.png".format(k))
    left = 273
    top = 64
    right = 741
    bottom = 592
    im1 = im.crop((left, top, right, bottom))
    im1.save("E:/picss/{}.png".format(k), "PNG")
    k+=1

