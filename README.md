# wapp_birthday_wisher
A python script for sending wishes to your Whats app contacts on their birthday

Save all our contacts along with their birth dates in birthdays.txt file. (Format : DD/MM) 
Then run birthday_greetings.py. 
The script will fetch the current date and then look for any birthdays on that day in the birthdays.txt file.
Then the script will send birthday greetings to all the contacts with birthdays on that day.
The message of greeting can be set as per requirement in the birthday_greetings.py file.

The script makes use of selenium library for accessing the browser. 
The choice of browser can be set in the script. (I have used chrome) 
Now make sure that you have required webdriver for the browser to be used. (Eg. chrome driver for chrome and geckodriver if using firefox) 

## Requirements
1. Python3
2. Selenium Library
3. Webdriver for browser to be used
