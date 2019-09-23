[TIMER](https://blog.csdn.net/qq_36350532/article/details/80622349)  
背景：JMeter常被定义成性能测试工具或是自动化测试工具，都没错，同时还可以作为接口测试及web功能测试，关键使用者根据业务需求选择使用其功能；      
性能测试方向：后起之秀JMeter与革命前辈Loadrunner的比较，JMeter测试工具的Timer可以根据实际场景设置思考时间，用于等待或是集合点同时并发操作；      
言归正传，我们来看看JMeter的Timer成员有哪些，及具体作用？  

****
## 目录
* [ConstantTimer](#ConstantTimer)
* [SynchronizingTimer](#SynchronizingTimer)
* [ConstantTimer](#ConstantTimer)

## ConstantTimer
 等待/思考时间  
![Constant Timer](https://img-blog.csdn.net/20171023200019459?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMTQ2NjQ2OQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)   
Name：恒定时间元件名称(可以理解是等待(思考)时间)，    
Comments：注释；    
Thread Delay（in milliseconds）：线程等待时间，单位毫秒；    
tips：用法(场景)，更真实的模拟用户场景，需要设置等待时间，或是等待上一个请求的时间，才执行，给sampler之间的思考时间；    

## SynchronizingTimer
集合时间(集合点)     
Name：Synchronizing Timer 同步定时器名称(集合点)   
Comments：注释，可以让定时器变得有意思，一目了然；   
Grouping：   
  Number of Simulated Users to Group by: 同组用户数量，设置为0，等效于线程组中的线程数(Number of Threads（users）)；   
  Timeout in milliseconds:超时时间，单位毫秒，默认为0；如果设置为0，定时器等待同组的用户数，如果设置大于0，将以等待的最大线程数运行；如果超时，等待的用户数没有到达，定时器将停止等待；如果超时了，设置并发的用户数大于线程数，那么脚本无法停止；   
tips：线程组用户数100，添加同步定时器， 


