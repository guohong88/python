import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')

print(help(test))

# # import  logging,copy
# # logging.error("error")
# # copy.deepcopy()
# import hashlib
# m=hashlib.md5()
# import hashlib
# m = hashlib.md5()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# print(m.digest(),m.hexdigest())

# coding=utf-8

import re

# 普通的匹配方式
# ret = re.match("嫦娥1号", "嫦娥1号发射成功")
# ret.group()
#
# ret = re.match("嫦娥2号", "嫦娥2号发射成功")
# ret.group()
#
# ret = re.match("嫦娥3号", "嫦娥3号发射成功")
# ret.group()
#
# # 使用\d进行匹配
# ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
# ret.group()
#
# ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
# ret.group()
#
# ret = re.match("嫦娥\d号", "嫦娥3号发射成功")
# print
# ret.group()

#coding=utf-8
# import re
# ret = re.match("[A-Z][a-z]*","Mmaaaaaa2323232323Mmaaaaa")#,re.MULTILINE)
# a=ret.group()
# print(a)
# ret = re.match("[A-Z][a-z]*","Aabcdef88")
# b=ret.group()
# print(b)

# ret = re.match("[a-zA-Z_]+[\w_]*","2_name")
# ret.group()

# ret = re.findall("[a-zA-Z_]+[\w_]*","2_name")
# print(ret)

# a=re.match(r".*\bver\b", "ho  ver abc").group()
# a=re.match(r".*\bver\b.*", "111ho   ver    abc 23").group()

# ret = re.match("[1-9]?\d$","1018")
# a = ret.group()
# print(a)

ret = re.match("\w{4,20}@(?:163|126|qq)\.com", "test@qq.com")
print(ret.group())#,ret.group(1))
ret = re.match(r"<html>(\w+)</html>", r"<html>hh</html>")
print(ret.group(),ret.group(1))

ret = re.match(r"<([A-Za-z]+)>(\w+)</(\1)>", r"<html>hh</html>")
print(ret.group(),ret.group(3))
# <html>hh</html>

ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
print(ret.group())


# http://www.interoem.com/messageinfo.asp?id=35
# http://3995503.com/class/class09/news_show.asp?id=14
# http://lib.wzmc.edu.cn/news/onews.asp?id=769
# http://www.zy-ls.com/alfx.asp?newsid=377&id=6
# http://www.fincm.com/newslist.asp?id=415

ret = re.findall(r"http://().()", "<html><h1>www.itcast.cn</h1></html>")
import