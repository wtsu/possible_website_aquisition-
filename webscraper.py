import selenium
from selenium import webdriver
chrome_path = 'C:\Users\willi\Desktop\python webscraper\selenium webscraper\chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_path)
url = "https://www.namecheap.com/domains/marketplace/buy-domains.aspx?page=1&size=100&excludehypen=false&excludenumber=false&maximumlength=6&priceRange=0%3a25%2c25%3a50%2c50%3a100%2c100%3a200%2c200%3a-1"
driver.get(url)
site_file = open("site.txt", "w")
price_file = open("prices.txt", "w")


maxNumOfPages = 6000; 
for pageId in range(2,maxNumOfPages+2):
	sites = driver.find_elements_by_css_selector(".six-cols.first")
	prices = driver.find_elements_by_class_name('price')
	for site in sites:
		site_file.write(site.text + " ,\n")
	price_file.write("domain name" + "\n")
	for price in prices:
		price_file.write(price.text + "\n")
	try:
		driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_ctl00_ctl00_base_content_web_base_content_home_content_page_content_left_ctl05_ctl00_pagerControl_Page_Next"]""").click()
	except:
		break

driver.quit()