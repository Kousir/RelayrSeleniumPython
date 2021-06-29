import time

class Search:
    searchbar_name= "q"
    searchbar_xpath="//input[@name='q']"
    searchbar_mic_xpath = "//div[@jscontroller='unV4T']"
    searchbar_suggestion_css = "div[jscontroller=J7ZZy]"
    empty_seachbar_click_xpath = "//ul/li[contains(@class,'ynRric')]"
    livemic_repord_xpath = "//div/span[@id='spchb']"
    livemic_exit_xpath = "//div/button[@id='spchx']"

    def __init__(self, driver):
        self.driver = driver

    def isSearchbarDisplayed(self):
        searchbar = self.driver.find_element_by_name(self.searchbar_name)
        if searchbar.is_displayed():
            assert True
            print("Search bar is displayed in home screen")
        else:
            print("Search bar is not displayed in home screen")
            assert False

    def searchbar(self, input):
        self.driver.find_element_by_name(self.searchbar_name).clear()
        time.sleep(1)
        self.driver.find_element_by_name(self.searchbar_name).send_keys(input)




    def clickOnSearchbar(self):
        self.driver.find_element_by_xpath(self.searchbar_xpath).click()
        trendsearches = self.driver.find_element_by_xpath(self.empty_seachbar_click_xpath)
        if trendsearches.is_displayed():
            assert True
            print("Top 10 trending searches are auto suggested")
        else:
            print("Trending searches are not displayed")
            assert False


    def isMicInputWorking(self):
        mic = self.driver.find_element_by_xpath(self.searchbar_mic_xpath)
        if mic.is_displayed():
            assert True
            print("Microphone for voice input is present in the search bar")
        else:
            print("Microphone for voice input is not displayed")
            assert False
        self.driver.find_element_by_xpath(self.searchbar_mic_xpath).click()





























