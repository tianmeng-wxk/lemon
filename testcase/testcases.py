import os
import sys

from common.common import ivercode

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('../')
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
        #hello world
    @data(['tianmeng','wxk111'],['wxk','wxk111'])
    @unpack
    def test_01(self,*data):
        self.case.browser("chrome")
        self.case.max_windows()
        self.case.visit("http://et.lemonban.com")
        sleep(2)
        self.case.click('/html/body/div[16]/div/div')
        sleep(1)
        self.case.click("/html/body/div[4]/div/ul[1]/li[1]/a")
        sleep(2)
        self.case.input('//*[@id="member_name"]', data[0])
        self.case.input('//*[@id="member_password"]', data[1])
        self.ele = self.case.locator("//*[@id='codeimage']")
        self.ele.screenshot(r"E:\lemon\common\verify.png")
        self.vercode=ivercode()
        self.case.input('//*[@id="captcha_normal"]', self.vercode)
        self.case.click('//*[@id="login_normal_form"]/div[5]/input')
        sleep(5)
        self.varidata=self.case.locator("/html/body/div[3]/div/ul[1]/li[1]/a").text
        self.assertEqual("tianmeng",self.varidata,msg="登录失败")

if __name__ == '__main__':
    unittest.main()



