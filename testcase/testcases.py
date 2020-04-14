from key_demo.keywork import Keyword
from time import sleep
import unittest
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_01(self):
        case = Keyword()
        case.browser("chrome")
        case.max_windows()
        case.visit("http://et.lemonban.com")
        sleep(3)
        case.click('/html/body/div[16]/div/div')
        sleep(1)
        case.click("/html/body/div[4]/div/ul[1]/li[1]/a")
        sleep(2)
        case.input('//*[@id="member_name"]','tianmeng')
        case.input('//*[@id="member_password"]','wxk111')
        case.input('//*[@id="captcha_normal"]',1111)
        case.click('//*[@id="login_normal_form"]/div[5]/input')
        sleep(5)

if __name__ == '__main__':
    unittest.main()



