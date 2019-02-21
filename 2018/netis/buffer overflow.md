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
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/3.png)
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/4.png)

## Harm
Can be accessed on the public network
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/netis/6.png)
