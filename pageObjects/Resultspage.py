from selenium.webdriver.common.action_chains import ActionChains

class Results:

    page_10_xpath = "//tbody/tr/td/a[@aria-label='Page 10']"
    settings_id = "abar_button_opt"

    def __init__(self, driver):
        self.driver = driver

#URL Validation
    def getpageurl(self):
        self.url = self.driver.current_url
        if "search?q=Munich+re" in self.url:
            assert True
            print("Correct result page is displayed")
            print(self.url)
        else:
            print("Incorrect result page displayed")
            assert False

#HTML Body validation
    def nextpage(self):
        element = self.driver.find_element_by_xpath(self.page_10_xpath)
        self.action = ActionChains(self.driver)
        self.action.move_to_element(element).click().perform()
        self.msg = self.driver.find_element_by_tag_name("body").text
        if "Munich Re Issues its First Green Bond in €1.25 Billion" in self.msg:
            assert True == True
            print("Successfully navigated to page 10")
        else:
            print("Error in finding the content")
            assert True == False

#JavaScript_Methods
    def jsback(self):
        self.driver.execute_script("window.history.go(-1)")

    def jscroll(self):
        settings = self.driver.find_element_by_id(self.settings_id)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", settings)
        print("Successfully navigated back to original results")












