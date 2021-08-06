# -*- coding: utf-8 -*-

import pymysql,datetime,time
from multiprocessing import Process
def sql(i):
    db = pymysql.connect(host='127.0.0.1', port=3066, user='TEST', passwd='TEST', db='db',charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    ziduan =''
    cursor.execute('set autocommit=1;	')
    cursor.execute('select * from '+ i + ' limit 1')
    re = cursor.fetchall()#先取表里的某条数据
    cursor.execute('show create table ' + i)
    re1 = cursor.fetchall()#取表结构
    prikey=[]
    intkey =[]
    strkey = []
    hashkey =[]
    deskey=[]
    file=''
    zhanweifustr=''
    for j in re1[0]['Create Table'].split('\n'):#取主键
        if 'PRIMARY KEY' in j:
            prikey.append(j.split('`')[1])
        elif 'dbpartition by' in j and 'HASH' in j:
            hashkey.append(j.split('`')[1].lower())
        elif 'description' in j and 'COMMENT' in j:
            deskey.append(j.split('`')[1])
    for j in prikey:#检查主键字段是否是属于数字
        for k in re1[0]['Create Table'].split('\n'):
            if j in k and 'PRIMARY KEY' not in k:
                if 'int' in k or 'decimal' in k and '(' in k and ')' in k and j == k.split('`')[1].split('`')[0]:
                    intkey.append(j)
                elif '(' in k and ')' in k and 'COMMENT' in k and j == k.split('`')[1].split('`')[0]:
                    strkey.append(j)
    for j in list(re[0].keys()):
        if j != list(re[0].keys())[-1]:
            ziduan = ziduan +'`' +j+'`,'
        else:
            ziduan = ziduan + '`' + j + '`)'

    for r in range(0,102):
        res = []
        for k in range(10000*r+1,10000*r+1+10000):
            zhi = ''
            zhilist=[]
            zhanweifu=[]
            for j in list(re[0].keys()):
                if j not in prikey and j not in hashkey and j !=list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\''+ str(re[0][j]) + '\','
                    zhilist.append(str(re[0][j]))
                    zhanweifu.append('%s')
                elif j not in prikey and j not in hashkey and j ==list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\''+ str(re[0][j]) + '\''
                    zhilist.append(str(re[0][j]))
                    zhanweifu.append('%s')
                elif j not in prikey and j in hashkey and j !=list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\''+  str(k) + '\','
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j not in prikey and j in hashkey and j ==list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\''+ str(k) + '\''
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j in intkey and j not in hashkey and j != list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + str(k) + ','
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j in intkey and j not in hashkey and j == list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + str(k) + '\''
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j in strkey and j not in hashkey and j != list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\'a'+ str(k) + '\','
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j in strkey and j not in hashkey and j == list(re[0].keys())[-1] and j not in deskey:
                    zhi = zhi + '\'a'+ str(k) + '\''
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j not in strkey and j not in hashkey and j != list(re[0].keys())[-1] and j in deskey:
                    zhi = zhi +  '\'people_idcard\','
                    zhilist.append(str(k))
                    zhanweifu.append('%s')
                elif j not in strkey and j not in hashkey and j == list(re[0].keys())[-1] and j in deskey:
                    zhi = zhi + '\'people_idcard\''
                    zhilist.append(str('people_idcard'))
                    zhanweifu.append('%s')
            zhanweifustr=','.join(zhanweifu)
            res.append(tuple(zhilist))
            # file=file+'\n'+'('+str(zhi)+'),'
        # print(sql)
        # print(zhi)
        # time.sleep(60)
        sql =  'insert into `' + i + '`(' + ziduan + ' VALUES ('+zhanweifustr+');'

        print(i + '表' + str(datetime.datetime.now()) + '开始插入数据')
        cursor.executemany(sql,res)
        print('pass')
    cursor.close()
    db.commit()
    db.close()
    print(i + '表' + str(datetime.datetime.now()) + '结束插入数据')
if __name__ =='__main__':
    tablename = ['table1_1']
    sql('table1_1')
    for i in tablename:
        t = Process(target=sql, args=(i,))
        t.start()
