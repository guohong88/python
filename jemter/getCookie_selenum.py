from selenium import webdriver
import requests
import time

def import_jquery():
    """
    通过执行jquery语句来判断当前网站是否具有jquery环境
    """
    try:  # 执行一段jquery测试代码
        driver.execute_script("$('body').text()")
    except Exception as e:  # 报错说明没有接入jquery环境，执行接入
        print('无jquery环境')
        # 请求jquery线上源码包
        file=open('D:\webderiver\jquery-2.1.3.min.js','rb+')
        resp=file.read()
# 直接执行jquery源码
        driver.execute_script(resp.decode())
        pass
    else:
        # 没报错说明接入了jquery环境
        print('error')

url='https://login.test123.com/login/'
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无界面模式
driver = webdriver.Chrome('D:\soft\chrome_plugin\webdriver\chromedriver.exe',chrome_options=options)
driver.get(url)
time.sleep(1)

driver.find_element_by_id('uid').send_keys('test520')
driver.find_element_by_id('password').send_keys('Pr0d1234')
driver.find_element_by_name('Submit').click()

cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookie_str = ';'.join(item for item in cookie)
print('cookie_str ',cookie_str)

# driver.execute_script(js)# 调用给搜索输入框标红js脚本
# driver.save_screenshot("redbaidu.png")#查看页面快照
# img = driver.find_element_by_xpath("//*[@id='lg']/img")#js隐藏元素，将获取的图片元素隐藏
# driver.execute_script('$(arguments[0]).fadeOut()',img)

# 向下滚动到页面底部
# driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

#查看页面快照
# driver.save_screenshot("2021052111111_nullbaidu.png")
driver.quit()a
