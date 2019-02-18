## netis buffer overflow
Product: netis WF2411-WF2880 (http://www.netis-systems.com/Home/info/id/2/hi/21.html)
version：The latest firmware --netis(WF2411)-V2.1.36123(http://www.netis-systems.com/Suppory/de_details/id/1/de/29.html)
Different device firmware version numbers may be different
Vulnerability location: file:  /bin/boa
function:user_auth->user_ok
Vulnerability Type: buffer overflow without login
## Vulnerability Description
There is a stack overflow vulnerability that does not require authentication
This can cause remote code execution
This vulnerability can be triggered by a normal get packet


##POC
