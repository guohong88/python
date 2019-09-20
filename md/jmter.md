# jmeter 控制器学习
[官方手册](http://jmeter.apache.org/usermanual/index.html)  
[官方 Controller](http://jmeter.apache.org/usermanual/component_reference.html#)  
[官方demo](https://jmeter.apache.org/demos/)    
## 1.1 If Controller使用  
[If Controller](https://www.jianshu.com/p/1e7a60ae49d1)  
如果（If）控制器，if控制器如果里面的条件不满足，是不执行里面的请求的，看用户自定义变量里的定义的methodName 的值是   
"${methodName}".equals("post")  ${__BeanShell(vars.get("run").equals("1"))}  
3 以后版本用beanshell 中vars.put(“run”,“f”); debugsample 响应数据中看不到输出值。  

对于新版本JMeter4.0，IF Controller的Expression输入框中不能直接填写判断条件的表达式，需要将利用__jexl3函数或__groovy函数将条件表达式求值计算为true/false才有效
根据警告信息，建议勾选Interpret Condition as Variable Expression?  
条件判断语句若是字符串，则需要用引号包围参数，如："FE_user" == "test002"  
选择"Evaluate for all children?"代表该If控制器在每个子节点执行时都会执行一次，不选择则代表If控制器只在入口执行一次  
If Controller之下的请求才会受到If控制器的约束，若是平级则不会受约束；因此建议将业务请求放在If控制器之下进行测试  
  
依从以上规则，填写到Expression输入框中的的内容，样式如：${__groovy("${FE_user}" == "test003",)}  
[wenzhang](https://blog.csdn.net/wx19900503/article/details/79206382)  
## 1.2 While Controller使用   
[官方控制器使用](http://jmeter.apache.org/usermanual/component_reference.html#)  
eg:  
${VAR} - where VAR is set to false by some other test element    
${__javaScript(${C}==10)}  
${__javaScript("${VAR2}"=="abcd")}  
${_P(property)} - where property is set to "false" somewhere else 

# jmeter 配置原件使用
## csv文件
1.	用户自定义变量生效的范围跟配置的路径有关。
配置到测试计划下面：所有的线程组都可以引用到自定义变量
配置到某个线程组下面：仅该线程组下面的sample可以引用配置的自定义变量
配置到某个线程（sample）下面自定义变量作用于就仅限于该线程了
2.	一般情况下，测试脚本中常用的系统变量都可以写到自定义变量里面（方便维护）

# 2 取样器的使用 
## 2.1Beanshell的教程
### Beanshell的基本语法
Beanshell的For循环与集合  
[数据类型转换](https://www.cnblogs.com/chongyou/p/10487853.html)      
[基本语法](https://blog.csdn.net/hujyhfwfh2/article/details/80862134)  
[建简易教程](https://www.cnblogs.com/puresoul/p/5092628.html)  
[简易接口测试](https://blog.csdn.net/weixin_34289744/article/details/89865692)
[接口测试实践](https://yq.aliyun.com/articles/486352)
[beanshell使用](https://www.cnblogs.com/puresoul/p/4949889.html)
[jmeter学习笔记]()

## JSON Extractor（Json提取器）
[详细讲解](https://blog.csdn.net/lluozh2015/article/details/54097449)
1.	Variable names(名称)：提取器的名称  
2.	Main sample and sub-samples：应用于主sample及子sample  
3.	Main sample only：默认的是这个，应用于主sample  
4.	Sub-samples only：应用于子sample  
5.	JMeter Variable Name to use：应用于变量命名的内容  
6.	JSON Path Expression：json表达式，一般用$.获取json解析信息中的内容如要获取一下json字段中的值可以用表达式$.config.config.id  

## 正则表达式提取器
[详细讲解](https://blog.csdn.net/quiet_girl/article/details/50724313)

# jemeter使用技巧 
## jmeter各种函数
[jmeter各种函数](https://blog.csdn.net/lijing742180/article/details/86579160)

## jemeter断言学习
[断言](https://blog.csdn.net/shuimengzhen/article/details/53067475)

## 非GUI界面运行(性能数据测试)    
性能数据测试时需要用命令行进行执行，在UI界面上执行时性能数据会不准确，UI界面的执行仅用于调试性能脚本，命令行下执行性能脚本的命令为：    
D:\ProgramData\apache-jmeter-4.0\bin>jmeter -n -t demotest.jmx -l test.jtl    
-h 帮助 -> 打印出有用的信息并退出    
-n 非 GUI 模式 -> 在非 GUI 模式下运行 JMeter    
-t 测试文件 -> 要运行的 JMeter 测试脚本文件    
-l 日志文件 -> 记录结果的文件    
-r 远程执行 -> 在Jmter.properties文件中指定的所有远程服务器    
-H 代理主机 -> 设置 JMeter 使用的代理主机    
-P 代理端口 -> 设置 JMeter 使用的代理主机的端口号    
## 聚合报告数据解读    
### 时间解读    
*Elapsed time    经过的时间(= Sample time = Load time = Response time )     
这个时间是我们测试常用的时间，也是整个请求的消耗时间，从发送到接收完成全程消耗的时间    
*Latency time  延迟时间    
 不常用，表示请求发送到刚开始接收响应时，这个时间<Elapsed time    
*Connection time  建立连接时间    
*吞吐量(Throughput) 
   吞吐量是指系统在单位时间内处理请求的数量。对于无并发的应用系统而言，吞吐量与响应时间成严格的反比关系，实际上此时吞吐量就是响应时间的倒数。前面已经说过，对于单用户的系统，响应时间（或者系统响应时间和应用延迟时间）可以很好地度量系统的性能，但对于并发系统，通常需要用吞吐量作为性能指标。    
*响应时间(RT) 响应时间是指系统对请求作出响应的时间。直观上看，这个指标与人对软件性能的主观感受是非常一致的，因为它完整地记录了整个计算机系统处理请求的时间    

### 聚合报告分析  
--------  
|Label  | samples |Average |Median |90%line |95%line|99%line|min|max|Error%|throughput|KE/sec|  
|---------  | --------- |--------- |--------- |--------- |---------|---------|---------|---------|---------|---------|---------|  
|request  | 66764 |1375 |1392 |2285 |3045|5644|6|10013|0.01%|202.7/sec|2.2|  
|总体  | 66764 |1375 |1392 |2285 |3045|5644|6|10013|0.01%|202.7/sec|2.2|     
#### 聚合报告分析解析 
*我的疑问1：吞吐量=202.7/sec 我的理解是--每秒处理202.7个请求 ，Average=1375我的理解是--处理完一个请求的平均时间：1375ms=1.375s  那么1s就只能处理一个请求。 那为什么吞吐量又是1s处理202.7个请求？  
答：Average=1375     这个的意思可以理解为一个线程处理完一个请求的平均时间：1375ms=1.375s    
而这个202.7/sec 就是一秒中可以处理202.7个请求 ，为什么会这样呢？因为你每秒钟会启动很多线程，每个线程都有可能完成一个请求，所以当线程数足够多的情况下就会有这样的结果。  
*Jmeter报告编辑  
通过修改jmeter.properties文件jmeter.save.saveservice.timestamp_format =yyyy/MM/dd HH:mm:ssss改变报告输出中timestamp格式  

## 线程启动与禁止
CTRAL+T
## jemete汉化 
1.启动后从菜单找到 options 》choose language 》chinese(中文界面展示)  
2.设置永久默认汉化：找到bin/jmeter.properties这个文件，在#language=en下面插入language=zh_CN
## 解决内存溢出  
找到jmeter.bat文件编辑    
调整参数：(参数的调整仅为参考，具体根据测试机的硬件配置来决定）  
调整堆内存的大小:将默认的set HEAP=-Xms512m -Xmx512m，调整为set HEAP=-Xms1024m -Xmx1024m；  
调整堆内存中新生带的大小:将默认的set NEW=-XX:NewSize=128m -XX:MaxNewSize=128m，调整为set NEW=-XX:NewSize=256m -XX:MaxNewSize=256m；  
调整堆内存中永久带的大小:将默认的set PERM=-XX:PermSize=64m -XX:MaxPermSize=128m，调整为set PERM=-XX:PermSize=128m -XX:MaxPermSize=256m；  
改完后需要重启jmeter。

## 解决ssl证书问题
[ssl](https://blog.csdn.net/ajiatutu/article/details/79569756)
首先要明确http和https的区别：            
1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用          
2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议        
3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443      
4、http的连接很简单，是无状态的；HTTPS协议是有ssl+http协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。  
使用jmeter访问访问https接口，需要添加ssl层证书。      
a可以使用在ie浏览器 输入要操作的地址 - 工具栏 - 安全 - 安全报告 - 查看报告点击详细信息 - 复制到文件，按提示逐步操作，将证书存储到本地文件夹    
![pic11](https://img-blog.csdn.net/20180315161655888?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2FqaWF0dXR1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)       
![pic2](https://img-blog.csdn.net/20180315161736230?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2FqaWF0dXR1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)     
b 证书下载后，运行cmd，在命令行把导出的证书打成.store。
![pic3](https://img-blog.csdn.net/20180315162029492?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2FqaWF0dXR1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)     
然后设置密令：  
![pic4](https://img-blog.csdn.net/20180315162117259?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2FqaWF0dXR1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
查看文件，此时已生成my.store  
jmeter脚本创建顺序：打开jmeter - 添加线程组- 在线程组下添加sampler - http请求，如下图所示：  
输入内容,示例接口为支付宝支付接口https://memberprod.alipay.com/account/reg/index.htm  
脚本如下所示：  
打开jmeter-选项 - ssl管理器  
导入my.store文件即可。  
![pic6](https://img-blog.csdn.net/20180315162316961?watermark/2/text/Ly9ibG9nLmNzZG4ubmV0L2FqaWF0dXR1/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)  
脚本如下所示，点击运行，提示输入密令，输入之前设置的密令即可。 
  
## JMeter第三方插件之Dummy Sampler

## 线程组类型
(1)	Setup Thread Group    
该种类型的线程组相当于一个预处理线程组，其任务会在Thread Group线程组前执行，可以用于设置一线预置条件。     
(2)	Teardown Thread Group    
Teardown Thread Group刚好和setUp Thread Group作用相反，它用于执行后置条件，可以用于测试任务完成后进行环境恢复等运作。   
(3)	Thread Group   
使用最多的就是这种类型的线程组，该线程组就是测试任务的载体。   
2.2	线程组配置   
 线程数   
用于配置线程数的个数，线程数越多，发送的消息量也越大，同时占用的系统资源也更多，但并不是线程数越多，发送的消息量就会越大，当达到某个最优值后，再增加线程，发送的消息量反而会变小，用户需要通过逐步探索，找到这个最优值。   
Ramp-Up Period   
可以理解为爬坡时间，该时间是指从任务启动开始，到创建完所有的线程，比如100个线程，所需要的时间。如果Ramp-Up Period设置为10，而Number of Threads设置为100， 则表示这个100个线程，要花费10秒，平均每秒会启动10个线程。这样做的目的是防止一次启动所有线程，会对被测系统造成巨大的冲击。   
通常情况下如果为了测试待测接口的并发能力可以把Ramp-Up Period设置为0，比如线程数设置为100时就表示同时向待测系统发送100个请求，用以观察待测系统的并发相应平均时间。   
循环次数   
   表示线程循环执行多少次，如果是进行调试测试工程，一般都会先设置成1次，而到正式执行压力测试时，会设置成“Forever”，即待久执行，由用户手工停止。
启动延迟：表示从当前时刻开始延迟多长时间开始运行。   
持续时间：设定运行时长。   
启动时间、结束时间：在特定的时间区段内执行工作，可以定时启动、结束测试。   
2.3	用户自定义变量   
在线程组上点击右键，选择添加->配置元件->用户定义的变量   
用户自定义变量配置说明：   
1.	用户自定义变量生效的范围跟配置的路径有关   。
配置到测试计划下面：所有的线程组都可以引用到自定义变量   
配置到某个线程组下面：仅该线程组下面的sample可以引用配置的自定义变量   
配置到某个线程（sample）下面自定义变量作用于就仅限于该线程了   
2.	一般情况下，测试脚本中常用的系统变量都可以写到自定义变量里面（方便维护）   


