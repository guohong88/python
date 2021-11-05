# coding=utf-8
# from locust import HttpUser
import os
from locust import HttpUser, TaskSet, task

import subprocess
# from gevent import monkey
# monkey.patch_all()
class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        mydata = "actionFlag=Authenticate&uid=0&pwd=2332"
        loginurl='https://login-url_login/login.do'
        myheader = {
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = self.client.post('https://login-url_login/login.do',data=mydata,verify=False,headers=myheader)
        print(r.status_code)
        # print(r.content)

    @task(1)
    def index(self):
        '''
        yheader2 = {
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "x - cbg - pss - rolecode": "Inventory_Management_COE",
        "x - cbg - victoria - rolename": "Inventory_Management_COE"
        }
        url='https://url_test.cplan:/v1/list/page/50/1?t=1626677475772&language=zh_CN&businessDomain=&buinessInvOrgCode=&businessEntityType=&businessInvManageEntityCode=&bussinessSubinvName=&erpSubinvName=&subinvTypeCode=&countryAlpha2Code=&subinvNameEnd=&mappingRelationActiveFlag=Y'
        mydata2 = '{"lang":"zh_CN"}'
        r2 = self.client.get(url,data=mydata2,verify=False,headers=myheader2)
        import  json
        file=json.loads(r2.content)
        print(r2.status_code)
        print(file)
        :return:
        '''
        pass


    @task(1)
    def index2(self):
        myheader2 = {
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "x - cbg - pss - rolecode": "Inventory_Management_COE",
        "x - cbg - victoria - rolename": "Inventory_Management_COE"
        }
        url='https://url_test.cplan:cplanio/cplanio/s1/list/page/50/1?t=1Y'
        mydata2 = '{"lang":"zh_CN"}'
        r2 = self.client.get(url,data=mydata2,verify=False,headers=myheader2)
        import  json
        file=json.loads(r2.content)
        print(r2.status_code)
        print(file)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    task_create = UserBehavior
    # task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000

if __name__ == '__main__':
    os.system("locust -f ./io_test.py  --host=https://login-.qq.com  ")  #  --web-host=127.0.0.1:8089   10.234.11.21
    # subprocess.Popen('locust -f ./locustfiletest.py --host=https://login-beta.123.com', shell=True)
    # host = 'http://123.com'
