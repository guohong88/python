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

# jemeter配置
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
# 2 取样器的使用 
## 2.1Beanshell的教程
### Beanshell的基本语法
Beanshell的For循环与集合  
[数据类型转换](https://www.cnblogs.com/chongyou/p/10487853.html)      
[基本语法](https://blog.csdn.net/hujyhfwfh2/article/details/80862134)  
[建简易教程](https://www.cnblogs.com/puresoul/p/5092628.html)  
