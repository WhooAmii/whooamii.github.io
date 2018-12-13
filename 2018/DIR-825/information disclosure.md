```
Dlink model DIR-825L, the latest firmware 2.10B1, there is a Information disclosure vulnerability.
This is due to the logical problem of permission judgment.
This will reveal the pin code, mac address, routing table, firmware version, update time, qos information, lan, wlan interface information of the device.
download link: ftp://ftp2.dlink.com/SECURITY_ADVISEMENTS/DIR-825/REVB/
Vulnerability location: file:  /sbin/httpd  function: do_widget_action

```
Vulnerability function:
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/1.png)


pin number
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/2.png)

route_table
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/4.png)

mac address,firmware information
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/5.png)

wlan interface information
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/6.png)

and
![images](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-825/3.png)
