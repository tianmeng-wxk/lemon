from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://et.lemonban.com")
# 添加Cookie
driver.add_cookie({'name': 'PHPSESSID', 'value': 'eti9uf7b04rqrmnf2pbtme7b5p'})
driver.add_cookie({'name': 'viewed_goods', 'value': 'cDOfAGdv5GsRud_4dceBU1p-d0bamsbdTtJeWyeN_5GNv9H8VxbNL0WeT94'})
# 刷新页面
driver.refresh()
# 等待两秒
sleep(2)
# 获取登录用户名并打印
username = driver.find_element_by_xpath("/html/body/div[4]/div/ul/li/a").text
print(username)
#关闭浏览器
driver.quit()