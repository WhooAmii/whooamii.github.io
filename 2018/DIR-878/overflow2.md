```
Dlink model DIR-878, the latest firmware 1.12B01, There is a stack overflow vulnerability, This vulnerability can be triggered by logging in with a blank password. So I think it equals no authentication required
This can cause remote code execution
download link: ftp://ftp2.dlink.com/PRODUCTS/DIR-878/REVA/
Vulnerability location: file:  /bin/prog.cgi
Vulnerability function：Different locations in different firmware versions
1.02B01: sub_421EA8
path:webssecurityhandler->sub_423fe4->sub_421EA8
1.12B01: sub_421BC8
Path: webssecurityhandler->sub_423e04->sub_421BC8

The attacker calls this function by sending a post packet to the http://ip/HNAP1/  page
.
Message header HNAP_AUTH length is not verified。At the same time, it uses the strncpy function to write to the stack, But the length of the copy is the length of the string entered by the user.Caused a stack overflow。
These devices are accessible on the Wan
```
post package 
1.login
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/8.png)
2.overflow
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/9.png)
Overflow offset:0x4dc
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/10.png)
results:
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/11.png)
