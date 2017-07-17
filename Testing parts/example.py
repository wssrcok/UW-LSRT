from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://newhuskies.cssauw.org")
            
elem = browser.find_element_by_link_text("CSSA Home")
print(elem.text)
# html_source = browser.page_source
# elem.get_attribute('innerHTML')
# print(elem)

#if "whatever" in html_source:
    # do something
#else:
    # do something else

browser.close()

