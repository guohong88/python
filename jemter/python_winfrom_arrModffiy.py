# -*- coding: utf-8 -*-
# @Time    : 2021/9/28 14:16
# @Author  : join

import PySimpleGUI as sg
import MySQLdb,pymysql,cx_Oracle

# 数据源
datasource = {'UAT': '',
              'SIT': '',
              'A1': '',
              'B1': ''}

sg.theme('BluePurple') #BluePurple Formula  Jarvis
#设置窗体里面的内容，是以列表样式
# layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]

eleAttr=['physical_or_info_subinv','obn_node_code','transit_subinv_flag','business_subinv_flag','erp_subinv_flag','business_subinv_active_flag','business_subinv_active_flag','active_flag']
index=['inventory_organization_code','subinv_name','datasource']
layout = [[sg.Text('  测试环境：', size=(15, 1)),sg.InputCombo(['UAT', 'SIT', 'A1', 'B1'],key='datasource',default_value='UAT', size=(20, 6))],
            # [sg.Single],
          [sg.Text('  库存组织：', size=(15, 1)), sg.InputText(key='inventory_organization_code', size=(20, 1),default_text='DG1'),
           sg.Text('  子库名称：', size=(20, 1)), sg.InputText(key='subinv_name', size=(20, 1),default_text='DG1*DG1110')],
            # [sg.Text('-'*2000, size=(500))],
          [sg.Text('信息/：', size=(15, 1)), sg.InputCombo(['infosubinv', 'physical'],key='physical_or_info_subinv',default_value='', size=(20, 6)),
           sg.Text('Outbound：', size=(18, 1)), sg.InputText(key='obn_node_code', size=(20, 1),default_text='CHN00067'),
            sg.Text('是否调：  ', size=(15, 1)), sg.InputCombo(['Y', 'N'],default_value='',key='transit_subinv_flag', size=(20, 6))
           ],

          [sg.Text('业务标识：', size=(15, 1)),sg.InputCombo(['Y', 'N'], key='business_subinv_flag', default_value='', size=(20, 6)),
           sg.Text('核算标识：', size=(18, 1)),sg.InputCombo(['Y', 'N'], key='erp_subinv_flag', default_value='', size=(20, 6)),
           sg.Text('业务子：', size=(15, 1)),sg.InputCombo(['Y', 'N'], key='business_subinv_active_flag', default_value='', size=(20, 6)),
           sg.Text('核算子：  ', size=(18, 1)),sg.InputCombo(['Y', 'N'], key='active_flag', default_value='', size=(20, 6)),
           ],

          [sg.Button('修改',key='update_flag',size=(15, 1)), sg.Exit(button_text='退出',key='Exit',size=(15, 1))]]

#窗口实例化 并设置窗口名，把内容放进去
window = sg.Window('子库属性更改', layout,auto_size_text=True)

#主题循环
while True:
	#读取按键和各个插件的值    window.read()窗口显示
	#event获取按键值
	#values[‘控件的KEY’]
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break
    elif  values.get('subinv_name','')=='' or  values.get('inventory_organization_code','')=='' or  values.get('datasource','')=='':
        sg.popup_error('库存组织/子库名称/测试环境 不能为空',auto_close_duration=2,auto_close=True)
    elif event == 'update_flag':
        print('update_flag','inter进入操作')
        lissql=[]
        attrUpdate={}
        where={
            'inventory_organization_code':values.get('inventory_organization_code'),
            'subinv_name': values.get('subinv_name'),
        }
        for i in values.keys():
            if (i in eleAttr ) and values.get(i,'')!='':
                # attrUpdate[i]=values.get(i)
                lissql.append("{}='{}'".format(i,values.get(i,'')))

        sql=r"update {} set {} where inventory_organization_code='{}' and subinv_name ='{}'".format('sms_subinv_basic_info_t',','.join(lissql) ,values.get('inventory_organization_code'),values.get('subinv_name'))
        if len(lissql)>0:
            print('inter len',sql)
            try:
                print('数据源2323',values.get('datasource',''),datasource.get(values.get('datasource',''),''))
                pw= 'Huawei#123%' if values.get('datasource','') in ['UAT','SIT'] else 'Huawei#_123'
                db_con_pp_sit = pymysql.connect(host=datasource.get(values.get('datasource',''),''), port=5066, user='cisc_io', passwd=pw,
                                                db='cisc_io',
                                                charset='utf8')
                cursor=db_con_pp_sit.cursor()
                # B=cursor.execute('SHOW TABELS')
                # print(B)
                A=cursor.execute(sql)
                db_con_pp_sit.commit()

                cursor.close()
                db_con_pp_sit.close()
                # cursor.execute(cursor.execute(sql))
                print(A)
            except Exception as d:
                print(d)
                sg.popup_error(d, auto_close_duration=1, auto_close=True)
                continue
                # raise  d
                # break
            sg.popup('更新成功',auto_close_duration=1,auto_close=True)

#窗口关闭
window.close()
