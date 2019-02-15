```
Dlink model DIR-878, the latest firmware 1.12B01,An attacker can log in with a blank password
download link: ftp://ftp2.dlink.com/PRODUCTS/DIR-878/REVA/
Vulnerability location: file:  /bin/prog.cgi
Vulnerability function：Different locations in different firmware versions
1.02B01: sub_42170C
path:webssecurityhandler->sub_423fe4-> sub_42170C
1.12B01: sub_42142C
Path: webssecurityhandler->sub_423e04->sub_42142C

The attacker calls this function by sending a post packet to the http://ip/HNAP1/  page
.
There is a problem with the authentication process of the program.
The program uses the strncmp function to compare passwords.
The length of the comparison is the length of the user input.
If the user input is empty, the verification passes。At the same time it can be used to blast passwords. Only need to blast 16*32 times
```
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/5.png)

post package 
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/6.png)
![image](https://github.com/WhooAmii/whooamii.github.io/blob/master/2018/DIR-878/7.png)

results:
This login status allows us to enter more function flow. Increased attack range
