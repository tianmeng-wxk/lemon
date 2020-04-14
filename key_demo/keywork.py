from selenium import webdriver
class Keyword(object):

    def browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()

    def visit(self, url):
        self.driver.get(url)

    def locator(self, loc):
        el = self.driver.find_element_by_xpath(loc)
        return el

    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    def click(self, loc):
        self.locator(loc).click()

    def quit(self):
        self.driver.quit()

    def max_windows(self):
        self.driver.maximize_window()









