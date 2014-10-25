from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
print("You should only see this if your test passed")
#It failed! I'm so proud!