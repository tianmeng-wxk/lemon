from key_demo.keywork import Keyword
from time import sleep
from ddt import ddt,data,unpack,file_data
import unittest
@ddt
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.case = Keyword()
    def tearDown(self) -> None:
        self.case.quit()
    @data(['tianmeng','wxk111','1111'],['wxk','wxk111','1234'])
    @unpack
    def test_01(self,name,pwd,vercode):
        self.case.browser("chrome")
        self.case.max_windows()
        self.case.visit("http://et.lemonban.com")
        sleep(2)
        self.case.click('/html/body/div[16]/div/div')
        sleep(1)
        self.case.click("/html/body/div[4]/div/ul[1]/li[1]/a")
        sleep(2)
        self.case.input('//*[@id="member_name"]', name)
        self.case.input('//*[@id="member_password"]', pwd)
        self.case.input('//*[@id="captcha_normal"]', vercode)
        self.case.click('//*[@id="login_normal_form"]/div[5]/input')
        sleep(5)

if __name__ == '__main__':
    unittest.main()



