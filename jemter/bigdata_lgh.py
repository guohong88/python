# tbl_2
# tbl_1
import MySQLdb,pymysql
import time
import random
import string
import sys

conn = pymysql.connect(host='', port=5066, user='224', passwd='123', db='224',charset='utf8')# sit数据源 1

cur = conn.cursor()

sleepTime=0.1  #休眠200ms
index=1000000
item=1000000
binintidnt=11111111111111111
binend=binintidnt+10 #1000*1000


def runInsert_tbl_1_01():
    # 批量插入方法
    total_count=0
    s = time.time()
    step=10000
    for j in range(0,101):
        # 主键自己设置
        # 主键自增
        data_list = [(genPlanId(), 'jj1', 'jj2', 'jj3', '223', '34', 'jm1', '2', '2', 2777, '2020-06-29 08:00:00', '2021-04-08 08:00:00', '2020-06-29 08:00:00', 'N', '2', '2', '2', '3', '4', '3 6', '4', '2', '34', None, '2021-06-26 15:16:13', None, '2021-06-26 15:16:13', None, "1", "2", 'N') for i in range(index+j*step,index+j*step+step)]
        sql = "INSERT INTO `tbl_1` ( `plan_id`, `i_o_code`, `s_c_id`, `og_ce`, `o_e`, `e`, `ee`, `w_num`, `i_num`, `m_qty`, `p_s_time`, `p_go_l_time`, `e_go_l_t`, `f_status`, `p_p_c`, `p_p_desc`, `production_planner_code`, `p_desc`, `p`, `proc_planner_name`, `mfg_p_code`, `mc`, `ry`, `cby`, `crte`, `las`, `laste`, `laion`, `dn`, `rk`, `dg`) " \
               "values(%s,%s,%s,%s,%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s,%s,%s)"
        total_count = cur.executemany(sql, data_list)
        test=cur.fetchall()
        print(test)
        conn.commit()
        time.sleep(2)
    cur.close()
    conn.close()
    e = time.time()
    print(total_count)
    print(e - s)


# 辅助类 (未封装)
def genPlanId():
    '''
    :return: 19901218A
    '''
    a1=(1976,1,1,0,0,0,0,0,0)        #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(1990,12,31,23,59,59,0,0,0) #设置结束日期时间元组（1990-12-31 23：59：59）
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳

    #随机生成10个日期字符串
    for i in range(0,1):
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y%m%d",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        # print(date)
    return date+str("C")
def generate_random_time():
    '''
    :return: '2021-04-01 01:36:06'
    '''
    a1=(1976,1,1,0,0,0,0,0,0)        #设置开始日期时间元组（1976-01-01 00：00：00）
    a2=(1990,12,31,23,59,59,0,0,0) #设置结束日期时间元组（1990-12-31 23：59：59）
    start=time.mktime(a1)    #生成开始时间戳
    end=time.mktime(a2)      #生成结束时间戳

    #随机生成10个日期字符串
    for i in range(0,1):
        t=random.randint(start,end)    #在开始和结束时间戳中随机取出一个
        date_touple=time.localtime(t)          #将时间戳生成时间元组
        date=time.strftime("%Y-%m-%d %H:%M:%S ",date_touple)  #将时间元组转成格式化字符串（1976-05-21）
        # print(date)
    return str(date)
def get_local_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    # print(random_str)
    return random_str
def getUuid():
    import uuid
    return  str(uuid.uuid4())

if __name__ == '__main__':
    '''
        # runInsert_Single_tbl_1()
        # runInsertSingle()
        # runInsert()  # 0.13s
        # print(genPlanId())
         # generate_random_time()
    '''
     runInsert_tbl_1()
    
