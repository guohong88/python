import MySQLdb,pymysql
import time
import random
import string
import sys

conn = pymysql.connect(host='127.0.0.1', port=3066, user='root', passwd='root', db='db',charset='utf8')# 数据源1 
# conn_uat = MySQLdb.connect(host='127.0.0.1', port=3066, user='root', passwd='root', db='db',charset='utf8') # 数据源2  
cur = conn.cursor()

sleepTime=0.2  #休眠200ms
index=1000000
item=1000000
binintidnt=11111111111111111
binend=binintidnt+10 #1000*1000

def runInsert_TABLE_24():
    '''
   table; table_test
   primary kye:  item_deduction_require_dtl_id  主键自增  范围 (0，18 446 744 073 709 551 615)
   dbpartition by HASH(`ITEM_DEDUCTION_REQUIRE_ID`);

    INSERT INTO `table_test` (`item_deduction_require_dtl_id`, `item_deduction_require_id`, `trans_type`, `item_number`, `item_version`, `scheduled_quantity`, `executed_quantity`, `open_quantity`, `qty_uom`, `trans_remarks`, `operation_code`, `inventory_organization_code`, `supply_subinventory_name`, `supply_locator_code`, `target_subinventory_name`, `target_locator_code`, `ppo_number`, `ppo_line_number`, `final_deal_flag`, `certificate_number`, `source_id`, `positive_marking`, `inventory_batch_number`, `delete_flag`, `created_by`, `creation_date`, `last_updated_by`, `last_update_date`, `last_update_version`, `description`)
    VALUES (141160, 552384994162196480, '35', '10100261', '', 20.0000000000, 20.0000000000, 0.0000000000, 'PCS', NULL, '10', 'DG1', '12BH30', 'KVHA5WX012', NULL, NULL, 'BSDPT141505', '176', '', '', NULL, NULL, '', 'N', NULL, '2021-05-12 17:07:37', 0, '2021-05-12 17:42:19', 2, NULL);

   :return: None
    '''
    # 批量插入方法
    total_count=0
    s = time.time()
    print('进入方法 ****',sys._getframe().f_code.co_name)
    step=10000
    for j in range(1,102):
        # strPre=generate_random_str(4)
        print('  第{} w数据  insert {}  '.format(j,sys._getframe().f_code.co_name))

        sql = "  INSERT INTO `table_test` (`item_deduction_require_id`, `trans_type`, `item_number`, `item_version`, `scheduled_quantity`, `executed_quantity`, `open_quantity`, `qty_uom`, `trans_remarks`, `operation_code`, `inventory_organization_code`, `supply_subinventory_name`, `supply_locator_code`, `target_subinventory_name`, `target_locator_code`, `ppo_number`, `ppo_line_number`, `final_deal_flag`, `certificate_number`, `source_id`, `positive_marking`, `inventory_batch_number`, `delete_flag`, `created_by`, `creation_date`, `last_updated_by`, `last_update_date`, `last_update_version`, `description`) " \
              "  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)   "

        # data_list = [(binintidnt+index+j*10000+i, 'Z00LGH', 'PDCG801125', None, '5TLA',str(string.ascii_letters[random.randint(0,51)])+str(item+j*10000+i), 'rere', 'N', '2021-08-05 00:34:47', 'N', -1, '2021-06-02 00:34:54', -1, '2021-08-05 00:34:47', 95, 'wx123')  for i in range(index+j*1000,index+j*1000+step)]
        data_list = [( binintidnt+index+j*10000+i, '35', '10100261', '', 20.0000000000, 20.0000000000, 0.0000000000, 'PCS', None, '10', '1AB1', '2323', 'kwh', None, None, '2323', '176', '', '', None, None, '', 'N', None, '2921-05-12 17:07:37', 0, '2021-05-12 17:42:19', 2, '测试性能数据：110') for i in range(index+j*1000,index+j*1000+step)]

        total_count = cur.executemany(sql, data_list)
        conn.commit()
        time.sleep(sleepTime)
    cur.close()
    conn.close()
    e = time.time()
    # print('{} insert COST TIME '.format('runInsert_Ppo_collaboration_task_log_12'),e - s)
    print('runInsert_TABLE_17 COST TIME  %s' % (e - s))


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
        # runInsertSingle()
        # runInsert()  # 0.13s
        # print(genPlanId())
         # generate_random_time()
    '''
    runInsert_TABLE_24()
