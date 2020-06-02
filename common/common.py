from PIL import Image
import requests

def ivercode():

    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
    data = {
        'user': 'wuqingfqng',
        'pass2': '6e8ebd2e301f3d5331e1e230ff3f3ca5',#密碼：wuqing&fqng
        "softid": "904357",
        "codetype": "1902"
    }
    userfile = open("E:\\lemon\\common\\verify.png","rb").read()
    userfile = {"userfile": ("E:\\lemon\\common\\verify.png", userfile)}
    res = requests.post("http://upload.chaojiying.net/Upload/Processing.php",data=data,files=userfile,headers=headers)
    res = res.json()
    vercode = res["pic_str"]
    return vercode






