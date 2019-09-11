# 2019/09/11
## popen(Unix，Windows)  
os.popen() 方法用于从一个命令打开一个管道。    
os.popen(command[, mode[, bufsize]])  
command -- 使用的命令。  
mode -- 模式权限可以是 'r'(默认) 或 'w'。  
bufsize -- 指明了文件需要的缓冲大小：返回一个文件描述符号为fd的打开的文件对象
## system(command)
os.system(command)，在一个子shell中运行command命令，并返回command命令执行完毕后的退出状态。
[补充](https://www.cnblogs.com/yizhenfeng168/p/6953330.html)

## git使用
[pycharm git 用法总结](https://www.cnblogs.com/xxtalhr/p/11154137.html)  
[pycharm git 解决冲突总结](https://blog.csdn.net/weixin_42174361/article/details/81265547)

测试计划
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="4.0" jmeter="4.0 r1823414">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="测试计划" enabled="true">
      <stringProp name="TestPlan.comments"></stringProp>
      <boolProp name="TestPlan.functional_mode">false</boolProp>
      <boolProp name="TestPlan.tearDown_on_shutdown">true</boolProp>
      <boolProp name="TestPlan.serialize_threadgroups">true</boolProp>
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">
        <collectionProp name="Arguments.arguments"/>
      </elementProp>
      <stringProp name="TestPlan.user_define_classpath"></stringProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="token" enabled="true">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="循环控制器" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <stringProp name="LoopController.loops">1</stringProp>
        </elementProp>
        <stringProp name="ThreadGroup.num_threads">1</stringProp>
        <stringProp name="ThreadGroup.ramp_time">1</stringProp>
        <boolProp name="ThreadGroup.scheduler">false</boolProp>
        <stringProp name="ThreadGroup.duration"></stringProp>
        <stringProp name="ThreadGroup.delay"></stringProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="token" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&#xd;
    &quot;auth&quot;: {&#xd;
        &quot;identity&quot;: {&#xd;
            &quot;password&quot;: {&#xd;
                &quot;user&quot;: {&#xd;
                    &quot;password&quot;: &quot;Huawei@123&quot;,&#xd;
                    &quot;domain&quot;: {&#xd;
                        &quot;name&quot;: &quot;ei_dlg_w00448499&quot;&#xd;
                    },&#xd;
                    &quot;name&quot;: &quot;ei_dlg_w00448499&quot;&#xd;
                }&#xd;
            },&#xd;
            &quot;methods&quot;: [&#xd;
                &quot;password&quot;&#xd;
            ]&#xd;
        },&#xd;
        &quot;scope&quot;: {&#xd;
            &quot;project&quot;: {&#xd;
                &quot;id&quot;: &quot;3adf48bad33342a4a2257cdeead814f9&quot;&#xd;
            }&#xd;
        }&#xd;
    }&#xd;
}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">100.95.181.176</stringProp>
          <stringProp name="HTTPSampler.port">31943</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">v3/auth/tokens</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="正则表达式提取器" enabled="true">
          <stringProp name="RegexExtractor.useHeaders">true</stringProp>
          <stringProp name="RegexExtractor.refname">token</stringProp>
          <stringProp name="RegexExtractor.regex">X-Subject-Token: ([\s\S]*)X-Request-Id</stringProp>
          <stringProp name="RegexExtractor.template">$1$</stringProp>
          <stringProp name="RegexExtractor.default"></stringProp>
          <stringProp name="RegexExtractor.match_number">1</stringProp>
        </RegexExtractor>
        <hashTree/>
        <BeanShellSampler guiclass="BeanShellSamplerGui" testclass="BeanShellSampler" testname="BeanShell Sampler" enabled="true">
          <stringProp name="BeanShellSampler.query">String token = bsh.args[0];
${__setProperty(token,${token},)}</stringProp>
          <stringProp name="BeanShellSampler.filename"></stringProp>
          <stringProp name="BeanShellSampler.parameters">${token}</stringProp>
          <boolProp name="BeanShellSampler.resetInterpreter">false</boolProp>
        </BeanShellSampler>
        <hashTree/>
      </hashTree>
      <ConfigTestElement guiclass="HttpDefaultsGui" testclass="ConfigTestElement" testname="HTTP请求默认值" enabled="true">
        <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="用户定义的变量" enabled="true">
          <collectionProp name="Arguments.arguments"/>
        </elementProp>
        <stringProp name="HTTPSampler.domain"></stringProp>
        <stringProp name="HTTPSampler.port"></stringProp>
        <stringProp name="HTTPSampler.protocol">https</stringProp>
        <stringProp name="HTTPSampler.contentEncoding"></stringProp>
        <stringProp name="HTTPSampler.path"></stringProp>
        <stringProp name="HTTPSampler.concurrentPool">6</stringProp>
        <stringProp name="HTTPSampler.connect_timeout"></stringProp>
        <stringProp name="HTTPSampler.response_timeout"></stringProp>
      </ConfigTestElement>
      <hashTree/>
      <HeaderManager guiclass="HeaderPanel" testclass="HeaderManager" testname="HTTP信息头管理器" enabled="true">
        <collectionProp name="HeaderManager.headers">
          <elementProp name="" elementType="Header">
            <stringProp name="Header.name">Content-Type</stringProp>
            <stringProp name="Header.value">application/json;charset=UTF-8</stringProp>
          </elementProp>
          <elementProp name="" elementType="Header">
            <stringProp name="Header.name">Accept</stringProp>
            <stringProp name="Header.value">application/json;charset=UTF-8</stringProp>
          </elementProp>
          <elementProp name="" elementType="Header">
            <stringProp name="Header.name">X-Auth-token</stringProp>
            <stringProp name="Header.value">${__P(token)}</stringProp>
          </elementProp>
        </collectionProp>
      </HeaderManager>
      <hashTree/>
      <Arguments guiclass="ArgumentsPanel" testclass="Arguments" testname="用户定义的变量" enabled="true">
        <collectionProp name="Arguments.arguments">
          <elementProp name="times" elementType="Argument">
            <stringProp name="Argument.name">times</stringProp>
            <stringProp name="Argument.value">1000</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
          <elementProp name="hour" elementType="Argument">
            <stringProp name="Argument.name">hour</stringProp>
            <stringProp name="Argument.value">${__timeShift(HH,,,,)}</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
          <elementProp name="min" elementType="Argument">
            <stringProp name="Argument.name">min</stringProp>
            <stringProp name="Argument.value">${__timeShift(mm,,PT20M,,)}</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
          <elementProp name="day" elementType="Argument">
            <stringProp name="Argument.name">day</stringProp>
            <stringProp name="Argument.value">${__timeShift(yyyy-MM-dd,,,,)}</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
          <elementProp name="day1" elementType="Argument">
            <stringProp name="Argument.name">day1</stringProp>
            <stringProp name="Argument.value">${__timeShift(yyyy-MM-dd,,P1D,,)}</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
          <elementProp name="IP" elementType="Argument">
            <stringProp name="Argument.name">IP</stringProp>
            <stringProp name="Argument.value">10.63.90.162</stringProp>
            <stringProp name="Argument.metadata">=</stringProp>
          </elementProp>
        </collectionProp>
      </Arguments>
      <hashTree/>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="长稳测试-bmm" enabled="false">
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="循环控制器" enabled="true">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <intProp name="LoopController.loops">-1</intProp>
        </elementProp>
        <stringProp name="ThreadGroup.num_threads">5</stringProp>
        <stringProp name="ThreadGroup.ramp_time">150</stringProp>
        <boolProp name="ThreadGroup.scheduler">false</boolProp>
        <stringProp name="ThreadGroup.duration"></stringProp>
        <stringProp name="ThreadGroup.delay"></stringProp>
      </ThreadGroup>
      <hashTree>
        <CSVDataSet guiclass="TestBeanGUI" testclass="CSVDataSet" testname="CSV 数据文件设置" enabled="true">
          <stringProp name="delimiter">\n</stringProp>
          <stringProp name="fileEncoding"></stringProp>
          <stringProp name="filename">D:\jmeter\test.csv</stringProp>
          <boolProp name="ignoreFirstLine">false</boolProp>
          <boolProp name="quotedData">false</boolProp>
          <boolProp name="recycle">true</boolProp>
          <stringProp name="shareMode">shareMode.group</stringProp>
          <boolProp name="stopThread">false</boolProp>
          <stringProp name="variableNames">testname</stringProp>
        </CSVDataSet>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm创建指标任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test&quot;,&quot;datawarehouse_id&quot;:&quot;ff80808169c080570169c1f8f74b0001&quot;,&quot;dw_name&quot;:&quot;dli0330ccc11111&quot;,&quot;metric_type&quot;:1,&quot;exe_sql&quot;:&quot;select count(1) from time0314&quot;,&quot;category_id&quot;:&quot;1&quot;,&quot;modifier&quot;:&quot;dlv_z00444943&quot;,&quot;tenant_id&quot;:&quot;d3bf4f9315ab46249e58b6699efe593a&quot;,&quot;db_name&quot;:&quot;test0314&quot;,&quot;queue_name&quot;:&quot;xx&quot;,&quot;owner&quot;:&quot;dlv_z00444943&quot;,&quot;creator&quot;:&quot;dlv_z00444943&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/metrics</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree>
          <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="正则表达式提取器" enabled="true">
            <stringProp name="RegexExtractor.useHeaders">false</stringProp>
            <stringProp name="RegexExtractor.refname">metricid</stringProp>
            <stringProp name="RegexExtractor.regex">&quot;id&quot; : &quot;(.*)&quot;,</stringProp>
            <stringProp name="RegexExtractor.template">$1$</stringProp>
            <stringProp name="RegexExtractor.default"></stringProp>
            <stringProp name="RegexExtractor.match_number">1</stringProp>
          </RegexExtractor>
          <hashTree/>
        </hashTree>
        <BeanShellSampler guiclass="BeanShellSamplerGui" testclass="BeanShellSampler" testname="BeanShell Sampler" enabled="false">
          <stringProp name="BeanShellSampler.query">String token = bsh.args[0];
${__setProperty(${},${metricid},)}</stringProp>
          <stringProp name="BeanShellSampler.filename"></stringProp>
          <stringProp name="BeanShellSampler.parameters">${metricid}</stringProp>
          <boolProp name="BeanShellSampler.resetInterpreter">false</boolProp>
        </BeanShellSampler>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm编辑指标任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test1&quot;,&quot;datawarehouse_id&quot;:&quot;ff80808169c080570169c1f8f74b0001&quot;,&quot;dw_name&quot;:&quot;dli0330ccc11111&quot;,&quot;exe_sql&quot;:&quot;select count(1) from time0314&quot;,&quot;category_id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;dlv_z00444943&quot;,&quot;tenant_id&quot;:&quot;d3bf4f9315ab46249e58b6699efe593a&quot;,&quot;db_name&quot;:&quot;test0314&quot;,&quot;queue_name&quot;:&quot;xx&quot;,&quot;id&quot;:&quot;${metricid}&quot;,&quot;previous_category_id&quot;:null,&quot;owner&quot;:&quot;dlv_z00444943&quot;,&quot;creator&quot;:&quot;dlv_z00444943&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/metrics/${metricid}</stringProp>
          <stringProp name="HTTPSampler.method">PUT</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm创建规则任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test&quot;,&quot;creator&quot;:&quot;dlv_z00444943&quot;,&quot;modifier&quot;:&quot;dlv_z00444943&quot;,&quot;native_expr&quot;:&quot;a&gt;1&quot;,&quot;metric_alias&quot;:&quot;{\&quot;a\&quot;:\&quot;${metricid}\&quot;}&quot;,&quot;expect_expr&quot;:&quot;&quot;,&quot;comparison_code&quot;:&quot;&quot;,&quot;comparison_value&quot;:&quot;&quot;,&quot;category_id&quot;:&quot;2&quot;,&quot;owner&quot;:&quot;dlv_z00444943&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/rules</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="正则表达式提取器" enabled="true">
          <stringProp name="RegexExtractor.useHeaders">false</stringProp>
          <stringProp name="RegexExtractor.refname">ruleid</stringProp>
          <stringProp name="RegexExtractor.regex">&quot;id&quot; : &quot;(.*)&quot;,</stringProp>
          <stringProp name="RegexExtractor.template">$1$</stringProp>
          <stringProp name="RegexExtractor.default"></stringProp>
          <stringProp name="RegexExtractor.match_number">1</stringProp>
        </RegexExtractor>
        <hashTree/>
        <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="正则表达式提取器" enabled="true">
          <stringProp name="RegexExtractor.useHeaders">false</stringProp>
          <stringProp name="RegexExtractor.refname">rulename</stringProp>
          <stringProp name="RegexExtractor.regex">&quot;name&quot; : &quot;(.*)&quot;,</stringProp>
          <stringProp name="RegexExtractor.template">$1$</stringProp>
          <stringProp name="RegexExtractor.default"></stringProp>
          <stringProp name="RegexExtractor.match_number">1</stringProp>
        </RegexExtractor>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm编辑规则任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test1&quot;,&quot;creator&quot;:&quot;dlv_z00444943&quot;,&quot;modifier&quot;:&quot;dlv_z00444943&quot;,&quot;native_expr&quot;:&quot;a&gt;1&quot;,&quot;metric_alias&quot;:&quot;{\&quot;a\&quot;:\&quot;${metricid}\&quot;}&quot;,&quot;expect_expr&quot;:&quot;&quot;,&quot;comparison_code&quot;:&quot;&quot;,&quot;comparison_value&quot;:&quot;&quot;,&quot;category_id&quot;:&quot;2&quot;,&quot;owner&quot;:&quot;dlv_z00444943&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/rules/${ruleid}</stringProp>
          <stringProp name="HTTPSampler.method">PUT</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm创建场景任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;version&quot;:0,&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test&quot;,&quot;category_id&quot;:&quot;3&quot;,&quot;rules&quot;:[{&quot;id&quot;:&quot;${ruleid}&quot;,&quot;name&quot;:&quot;${rulename}&quot;,&quot;rule_alias&quot;:&quot;A&quot;}],&quot;check_expr&quot;:&quot;#${ruleid}&quot;,&quot;expression&quot;:&quot;A&quot;,&quot;run_type&quot;:4,&quot;alarm_level&quot;:3,&quot;alarm_type&quot;:0,&quot;topic_id&quot;:&quot;urn:smn:southchina:d3bf4f9315ab46249e58b6699efe593a:ym&quot;,&quot;alarm_on&quot;:true,&quot;cron&quot;:&quot;00 */15 00-23 * * ?&quot;,&quot;exclude_cron&quot;:null,&quot;schedule&quot;:{&quot;activation_date_start&quot;:&quot;${day}&quot;,&quot;activation_date_end&quot;:&quot;&quot;,&quot;schedule_period&quot;:1,&quot;start_time&quot;:&quot;00:00:00&quot;,&quot;interval_value&quot;:&quot;15&quot;,&quot;end_time&quot;:&quot;23:59:59&quot;,&quot;specific_time&quot;:&quot;00:00:00&quot;,&quot;select_time&quot;:&quot;&quot;}}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/businesses</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <RegexExtractor guiclass="RegexExtractorGui" testclass="RegexExtractor" testname="正则表达式提取器" enabled="true">
          <stringProp name="RegexExtractor.useHeaders">false</stringProp>
          <stringProp name="RegexExtractor.refname">businessid</stringProp>
          <stringProp name="RegexExtractor.regex">&quot;id&quot; : (.*),</stringProp>
          <stringProp name="RegexExtractor.template">$1$</stringProp>
          <stringProp name="RegexExtractor.default"></stringProp>
          <stringProp name="RegexExtractor.match_number">1</stringProp>
        </RegexExtractor>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm编辑场景任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;name&quot;:&quot;${testname}&quot;,&quot;description&quot;:&quot;test1&quot;,&quot;schedule&quot;:{&quot;activation_date_start&quot;:&quot;2019-04-15&quot;,&quot;activation_date_end&quot;:&quot;&quot;,&quot;schedule_period&quot;:1,&quot;start_time&quot;:&quot;00:00:00&quot;,&quot;interval_value&quot;:&quot;15&quot;,&quot;end_time&quot;:&quot;23:59:59&quot;,&quot;specific_time&quot;:&quot;00:00:00&quot;,&quot;select_time&quot;:&quot;&quot;},&quot;version&quot;:0,&quot;run_type&quot;:4,&quot;cron&quot;:&quot;00 */15 00-23 * * ?&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/businesses/${businessid}</stringProp>
          <stringProp name="HTTPSampler.method">PUT</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm启动场景任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;action&quot;:&quot;startSchedule&quot;,&quot;business_id&quot;:&quot;${businessid}&quot;,&quot;run_type&quot;:2}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain"></stringProp>
          <stringProp name="HTTPSampler.port"></stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/businesses/action</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <TestAction guiclass="TestActionGui" testclass="TestAction" testname="Test Action" enabled="true">
          <intProp name="ActionProcessor.action">1</intProp>
          <intProp name="ActionProcessor.target">0</intProp>
          <stringProp name="ActionProcessor.duration">10000</stringProp>
        </TestAction>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm停止场景任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;action&quot;:&quot;stopSchedule&quot;,&quot;business_id&quot;:&quot;${businessid}&quot;}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain"></stringProp>
          <stringProp name="HTTPSampler.port"></stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/businesses/action</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <TestAction guiclass="TestActionGui" testclass="TestAction" testname="Test Action" enabled="true">
          <intProp name="ActionProcessor.action">1</intProp>
          <intProp name="ActionProcessor.target">0</intProp>
          <stringProp name="ActionProcessor.duration">5000</stringProp>
        </TestAction>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm删除场景任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">{&quot;ids&quot;:[&quot;${businessid}&quot;]}</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/businesses</stringProp>
          <stringProp name="HTTPSampler.method">DELETE</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm删除规则任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value"></stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/rules/${ruleid}</stringProp>
          <stringProp name="HTTPSampler.method">DELETE</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="HTTP请求-bmm删除指标任务" enabled="true">
          <boolProp name="HTTPSampler.postBodyRaw">true</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments">
            <collectionProp name="Arguments.arguments">
              <elementProp name="" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value"></stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">${IP}</stringProp>
          <stringProp name="HTTPSampler.port">20032</stringProp>
          <stringProp name="HTTPSampler.protocol"></stringProp>
          <stringProp name="HTTPSampler.contentEncoding"></stringProp>
          <stringProp name="HTTPSampler.path">bmm/v1/d3bf4f9315ab46249e58b6699efe593a/metrics/${metricid}</stringProp>
          <stringProp name="HTTPSampler.method">DELETE</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          <stringProp name="HTTPSampler.embedded_url_re"></stringProp>
          <stringProp name="HTTPSampler.connect_timeout"></stringProp>
          <stringProp name="HTTPSampler.response_timeout"></stringProp>
        </HTTPSamplerProxy>
        <hashTree/>
      </hashTree>
      <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="察看结果树" enabled="true">
        <boolProp name="ResultCollector.error_logging">false</boolProp>
        <objProp>
          <name>saveConfig</name>
          <value class="SampleSaveConfiguration">
            <time>true</time>
            <latency>true</latency>
            <timestamp>true</timestamp>
            <success>true</success>
            <label>true</label>
            <code>true</code>
            <message>true</message>
            <threadName>true</threadName>
            <dataType>true</dataType>
            <encoding>false</encoding>
            <assertions>true</assertions>
            <subresults>true</subresults>
            <responseData>false</responseData>
            <samplerData>false</samplerData>
            <xml>false</xml>
            <fieldNames>true</fieldNames>
            <responseHeaders>false</responseHeaders>
            <requestHeaders>false</requestHeaders>
            <responseDataOnError>false</responseDataOnError>
            <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
            <assertionsResultsToSave>0</assertionsResultsToSave>
            <bytes>true</bytes>
            <sentBytes>true</sentBytes>
            <threadCounts>true</threadCounts>
            <idleTime>true</idleTime>
            <connectTime>true</connectTime>
          </value>
        </objProp>
        <stringProp name="filename"></stringProp>
      </ResultCollector>
      <hashTree/>
      <ResultCollector guiclass="StatVisualizer" testclass="ResultCollector" testname="聚合报告" enabled="true">
        <boolProp name="ResultCollector.error_logging">false</boolProp>
        <objProp>
          <name>saveConfig</name>
          <value class="SampleSaveConfiguration">
            <time>true</time>
            <latency>true</latency>
            <timestamp>true</timestamp>
            <success>true</success>
            <label>true</label>
            <code>true</code>
            <message>true</message>
            <threadName>true</threadName>
            <dataType>true</dataType>
            <encoding>false</encoding>
            <assertions>true</assertions>
            <subresults>true</subresults>
            <responseData>false</responseData>
            <samplerData>false</samplerData>
            <xml>false</xml>
            <fieldNames>true</fieldNames>
            <responseHeaders>false</responseHeaders>
            <requestHeaders>false</requestHeaders>
            <responseDataOnError>false</responseDataOnError>
            <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
            <assertionsResultsToSave>0</assertionsResultsToSave>
            <bytes>true</bytes>
            <sentBytes>true</sentBytes>
            <threadCounts>true</threadCounts>
            <idleTime>true</idleTime>
            <connectTime>true</connectTime>
          </value>
        </objProp>
        <stringProp name="filename"></stringProp>
      </ResultCollector>
      <hashTree/>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
