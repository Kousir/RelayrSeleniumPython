import time
import openpyxl
from pageObjects.Homepage import Search
from pageObjects.Voicesearchpage import Voicesearch
from pageObjects.Autosuggestions import AutoSuggest
from pageObjects.Resultspage import Results
from utility.readProperties import Readconfig
from utility.customLogger import loggen
from utility import excelHandler


class TestSearchUI:
    URL = Readconfig.getURL()
    logger = loggen.loggen()

#Test methods to validating UI

    def test_searchUI(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        self.searchbar = Search(self.driver)

        self.logger.info("***********Test 1************")
        self.logger.info("***********Validating search bar visibility in homepage************")
        self.searchbar.isSearchbarDisplayed()
        time.sleep(1)

        self.logger.info("***********Test 2************")
        self.logger.info("***********Validating auto suggestion visibility in homepage************")
        self.searchbar.clickOnSearchbar()
        time.sleep(2)

        self.logger.info("***********Test 3************")
        self.logger.info("***********Validating accessibility in homepage************")
        self.searchbar.isMicInputWorking()
        time.sleep(2)

        self.logger.info("***********Test 4************")
        self.logger.info("***********Validating UI in voice search page************")
        self.voice = Voicesearch(self.driver)
        self.voice.voicesearchvalidate()
        self.driver.close()

#Test methods to validate functionality

class TestSearchUX:
    URL = Readconfig.getURL()
    logger = loggen.loggen()
    path = "./testData/Relayrdata.xlsx"

    def test_searchbytype(self, setup):
        self.driver = setup
        self.driver.get(self.URL)

        self.logger.info("***********Test 5************")
        self.logger.info("************Sending req to the search bar***********")
        self.type = Search(self.driver)
        self.rows = excelHandler.getRowCount(self.path, 'Sheet1')
        print("No of rows in excel:", self.rows)
        for r in range(2, self.rows):
            self.logger.info("************Sending data from excel file***********")
            self.item1 = excelHandler.readData(self.path, 'Sheet1', r, 1)
            self.type.searchbar(self.item1)
            time.sleep(2)
        self.suggest = AutoSuggest(self.driver)
        self.suggest.suggestionbox()

        self.logger.info("***********Test 6************")
        self.logger.info("************Sending req to the search bar***********")
        self.driver.save_screenshot(".\\Screencaptures\\" + "Autosuggestio.png")
        time.sleep(2)
        self.suggest.clearsuggestion()
        for r in range(3, self.rows+1):
            self.item2 = excelHandler.readData(self.path, 'Sheet1', r, 1)
            self.logger.info("************Sending new req to the search bar***********")
            self.type.searchbar(self.item2)
        time.sleep(2)
        self.logger.info("************Searching for the input***********")
        self.suggest.submit()
        time.sleep(1)

        self.logger.info("************Test 7***********")
        self.logger.info("************Validating URL***********")
        self.result = Results(self.driver)
        self.result.getpageurl()

        self.logger.info("************Test 8***********")
        self.logger.info("************Navigating to a different page. HTML content validation***********")
        self.result.nextpage()
        time.sleep(2)

        self.logger.info("************Test 9***********")
        self.logger.info("************Navigating back to the original search result page***********")
        self.result.jsback()
        time.sleep(1)
        self.result.jscroll()
        self.driver.close()







































