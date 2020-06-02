from selenium import webdriver
import requests
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

    def ivercode(driver):
        ele = driver.locator("//*[@id='codeimage']")
        ele.screenshot("E:\\pycharm\\testingshop\\vercode_img\\verify.png")
        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
        data = {
            'user': 'wuqingfqng',
            'pass2': '6e8ebd2e301f3d5331e1e230ff3f3ca5',  # 密碼：wuqing&fqng
            "softid": "904357",
            "codetype": "1902"
        }
        userfile = open("E:\\pycharm\\testingshop\\vercode_img\\verify.png", "rb").read()
        userfile = {"userfile": ("E:\\pycharm\\testingshop\\vercode_img\\verify.png", userfile)}
        res = requests.post("http://upload.chaojiying.net/Upload/Processing.php", data=data, files=userfile,
                            headers=headers)
        res = res.json()
        vercode = res["pic_str"]
        return vercode









