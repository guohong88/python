Sqlflow    
https://www.cnblogs.com/liubinsh/p/7568423.html  
性能测试工具locust (python可以关注)                                                         https://www.cnblogs.com/shenh/p/12424990.html
  MySQL存储过程中的3种循环,存储过程的基本语法,                                         https://www.cnblogs.com/duanxz/p/3936618.html      
  https://blog.csdn.net/u012758088/article/details/78082885                     MySQL系列—全文检索（fulltext）使用   SELECT * FROM `student` WHERE MATCH(`name`,`address`) AGAINST('聪 广东')
http://blog.itpub.net/29734436/viewspace-2137628/                          MySQL使用profile分析语句性能消耗
https://github.com/orangle/study-resources/blob/master/mysql.md  MySQL/博客
https://segmentfault.com/a/1190000008131735                                   Explain 使用分析
https://blog.csdn.net/qq_39147299/article/details/109149796 大文件断点续传 
https://www.cnblogs.com/sumsen/archive/2013/03/04/2943471.html  dblink使用
导入jq本地环境
def import_jquery():
    """
    通过执行jquery语句来判断当前网站是否具有jquery环境
   """
    try:  # 执行一段jquery测试代码
        driver.execute_script("$('body').text()")
    except Exception as e:  # 报错说明没有接入jquery环境，执行接入
        print('无jquery环境')
        # 请求jquery线上源码包或本地包 resp = requests.get(r'https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.min.js')
        file=open('D:\webderiver\jquery-2.1.3.min.js','rb+')
        resp=file.read()
        driver.execute_script(resp.decode())
        pass
    else:
        # 没报错说明接入了jquery环境
        print('error')
 
https://blog.csdn.net/minzhisocute/article/details/112850708   Python学习路线图（2021最新版）
https://blog.csdn.net/python36/article/details/84105698 
https://blog.csdn.net/makesomethings/article/details/103648119?spm=1001.2014.3001.5502  调用无头浏览器获取cookie信息 以及使用   
https://blog.csdn.net/makesomethings/article/details/103112892        链家网爬虫 Selenium+Requests多线程  
https://blog.csdn.net/makesomethings/article/details/103059509?spm=1001.2014.3001.5501             链家网爬虫 Selenium+Requests多线程   
https://blog.csdn.net/makesomethings?type=blog webdriver  爬虫常见问题解决
https://blog.csdn.net/soonfly/article/details/78361819  yield深刻理解  
https://blog.csdn.net/xie_0723/article/details/53925076      
https://www.cnblogs.com/linxiyue/p/7911916.html    
https://blog.csdn.net/makesomethings/article/details/102961362?spm=1001.2014.3001.5502       
书籍推荐 
【书籍推荐】入侵的艺术鲍丽宁
【书籍推荐】软件调试 第2版鲍丽宁
【书籍推荐】渗透测试基础：可靠性安全审计实践指南鲍丽宁
【书籍推荐】开发者测试鲍丽宁
【书籍推荐】敏捷软件测试:测试人员与敏捷团队的实践指南鲍丽宁
【书籍推荐】基于模型的测试：一个软件工艺师的方法鲍丽宁
【书籍推荐】XSS跨站脚本攻击剖析与防御鲍丽宁
【书籍推荐】漏洞战争——软件漏洞分析精要鲍丽宁       
