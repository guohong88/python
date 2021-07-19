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
        mydata = "actionFlag=active"
        loginurl='https://login-beta.huawei.com/login/login.do'
        myheader = {
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        r = self.client.post('https://login.baidu.com/login/login.do',data=mydata,verify=False,headers=myheader)
        print(r.status_code)
        # print(r.content)

    @task(1)
    def index(self):
        myheader2 = {
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "x - cbg - pss - rolecode": "role2",
        "x - cbg - victoria - rolename": "role1"
        }
        url='www.baidu.com/tianqi'
        mydata2 = '{"lang":"zh_CN"}'
        r2 = self.client.get(url,data=mydata2,verify=False,headers=myheader2)        
        print(r2.status_code)
        print(r2.content)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    task_create = UserBehavior
    # task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000

if __name__ == '__main__':
    os.system("locust -f ./io_test.py  --host=https://www.baidu.com  ")  #  --web-host=127.0.0.1:8089   
    # subprocess.Popen('locust -f ./locustfiletest.py --host=https://login.baidu.com', shell=True)
   
