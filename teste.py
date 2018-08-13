from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://cbjj.com.br/calendario-2019/")
body = browser.find_element_by_id("mainContent")
print(body.text)

filename = 'C:\Selenium\data.txt'

fileout = open(filename, 'w')
fileout.write(body.text)
fileout.close()
