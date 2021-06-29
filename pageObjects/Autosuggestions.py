from selenium.webdriver.common.action_chains import ActionChains

class AutoSuggest:

    """Locators"""

    results_xpath = "//ul[@role='listbox']"
    autosuggested_top10_xpath = "//ul[@jsname='erkvQe']//li/descendant::div[@class='wM6W7d']"
    searchbar_clear_xpath = "//span[@jsname='itVqKe']"
    google_search_name = "btnk"

    """
    Defining a constructor
    """

    def __init__(self, driver):
        self.driver = driver

    """
    Action method - Printing the list elements & length of the list 
    """

    def suggestionbox(self):
        suggestion = self.driver.find_element_by_xpath(self.autosuggested_top10_xpath)
        suggestions = self.driver.find_elements_by_xpath(self.autosuggested_top10_xpath)
        if suggestion.is_displayed():
            assert True
            print(len(suggestions), "is the total no of suggestions")
            for result in suggestions:
                print(result.text)
            print("Top 10 results printed")
        else:
            assert False

    def clearsuggestion(self):
        clear = self.driver.find_element_by_xpath(self.searchbar_clear_xpath)
        if clear.is_displayed():
            assert True
            print("Clearing the input using x button in search bar")
            self.driver.find_element_by_xpath(self.searchbar_clear_xpath).click()
        else:
            assert False

    """
    'ActionChains' method to find the element in the page that is not visible 
    """

    def submit(self):
        element = self.driver.find_element_by_xpath("//input[@value='Google Search']")
        self.action = ActionChains(self.driver)
        self.action.move_to_element(element).click().perform()




















