import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


print('Starting script')
print('Hello Aman')
print('Today is ' + time.strftime("%d/%m"))
print('Searching for birthdays')
contactNames = ""

fp = open("birthdays.txt","r")
for line in fp:
    if str(time.strftime("%d/%m")) in line:
        temp = line.split()
        contactNames = contactNames +" "+ temp[1]
print("Todays birthdays : ")
print (contactNames)
contactNames = contactNames.split()
driver = webdriver.Chrome()
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

print('WhatsApp running...')

message = "Happy birthday!"
for  contactName in contactNames:
    print(contactName)
    contact_xpath = '//span[@title = "'+contactName+'" ]'
    select_contact = wait.until(EC.presence_of_element_located((By.XPATH, contact_xpath)))
    select_contact.click()

    print('Sending greetings to '+ contactName)
    input_xpath = '//div[@class="input"][@data-tab="1"][@dir="auto"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))

    input_box.send_keys(message + Keys.ENTER)

    print('Greetings sent successfully')
print('Closing script')

