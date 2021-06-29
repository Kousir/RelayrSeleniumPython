import time

class Voicesearch:

    """Locators"""

    livemic_repord_xpath = "//span[@id='spchb']"
    livemic_exit_xpath = "//div/button[@id='spchx']"

    """
    Defining a constructor  
    """

    def __init__(self, driver):
        self.driver = driver

    """
    Action methods to handle mic permission & UI elements 
    """

    def voicesearchvalidate(self):
        livemic = self.driver.find_element_by_xpath(self.livemic_repord_xpath)
        if livemic.is_displayed():
            assert True
            print("Microphone permission handled successfully")
        else:
            print("Please handle permission popup")
            assert False

        livemicexit = self.driver.find_element_by_xpath(self.livemic_exit_xpath)
        if livemicexit.is_displayed():
            assert True
            print("Closing the voice search page, by tapping on X")
            self.driver.find_element_by_xpath(self.livemic_exit_xpath).click()
            time.sleep(1)
        else:
            print("Close(X) button on top-right corner is not present")
            assert False
