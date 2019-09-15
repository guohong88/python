# 1jmeter学习
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
## 1.1 While Controller使用   
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
  
