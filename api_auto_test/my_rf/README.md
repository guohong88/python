# 基于requests + unittest的python版接口自动化测试框架
***

更多测试干货，请访问：[从测试小白到高级全栈测试修炼之路（自动化 、性能、测开、安全）](https://www.cnblogs.com/uncleyong/p/10530261.html)：https://www.cnblogs.com/uncleyong/p/10530261.html
<br>
更多测试干货，请关注：**微信公众号：全栈测试笔记**
<br>
![微信公众号：全栈测试笔记](https://files-cdn.cnblogs.com/files/uncleyong/qzcsbj2.bmp)


#### 介绍

    基于requests + unittest的python版接口自动化测试框架
        0. 前置知识储备：需要python基础，可以参考：https://www.cnblogs.com/UncleYong/category/1188224.html
        1. test_case下的用例只是简单演示，并没有用到这个框架中的所有功能模块，比如封装的db_operate.py、redis_operate.py等都没用到
        2. 数据分离，可以分离到excel中，大家就自己发挥优化吧，^_^

#### 软件架构

    1. bin: 可执行文件，程序入口
    2. conf: 配置文件
    3. core: 核心文件
    4. db_fix: 数据库操作
    5. log: 日志文件
    6. mockserver：测试用例需要用到的mock服务
    7. reprot: 测试报告
    8. test_case: 测试用例（数据文件），# testSelect.py文件用例对应的mock项目在mockserver目录下
    9. README.md: 说明文件


#### 环境模块说明

    python3.6 + requests + unittest + cx_oracle + HTMLTestRunner + os + sys + json + time + redis

        1. Python3.6，解释器环境
        2. requests，模拟用户发送http协议get或者post类型请求
        3. unittest，组织运行测试用例
        4. cx_oracle，操作数据库，每次请求前，连接数据库，清除垃圾数据，初始化测试数据（如果是mysql，一样的思路，模块是pymysql）
        5. HTMLTestRunner，生成html格式报告模板
        6. os，获取路径
        7. sys，设置环境变量
        8. json，对服务器返回的字符串转换为字典，方便做断言
        9. time，时间戳，生成的报告名称是：time_report.html
        10. redis，操作redis增加短信验证码，模拟获取短信验证码

#### 安装教程

    1. xxxx
    2. xxxx
    3. xxxx

#### 使用说明

    1. xxxx
    2. xxxx
    3. xxxx


#### 待扩展功能

    集成jenkins，jenkins中执行命令：
        windows环境下，如果脚本在：C:\test，执行python3 C:\test\bin\my_run.py %BUILD_NUMBER%
        linux环境下，如果脚本在：C:\test，执行python3 /opt/my_rf/bin/my_run.py $BUILD_NUMBER
        输出的报告名称为：【6】2017-09-11_09_09_56_report.html，最前面的数字为第多少次构建


#### 更新历史

    2019-04-03 v1.4 增加可读性的优化和mockserver
    2018-05-17 v1.3 优化redis操作
    2018-04-25 v1.2 新增oracle数据库操作
    2018-04-24 v1.1 新增日志调试日志，可屏幕和文件输出日志
    2018-04-12 v1.0 基础版

#### 参与贡献
    感谢xxxx






