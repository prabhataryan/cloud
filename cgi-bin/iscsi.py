!/usr/bin/python
import os,commands,cgi
print "content-type: text/html"

print "";

data=cgi.FieldStorage()

cl_ip = cgi.os.environ["REMOTE_ADDR"]

userid=data.getvalue("userid")

size=data.getvalue("size")

password=data.getvalue("password")

commands.getstatusoutput("sudo iptables -F")
commands.getstatusoutput("sudo useradd "+userid)
commands.getstatusoutput("sudo echo "+password+" | sudo passwd "+userid+"  --stdin")
commands.getstatusoutput("sudo  lvcreate    -V"+size+"G  --name "+userid+"  --thin vg1/pool1")

f=open("/etc/tgt/targets.conf","a")

f.write("\n<target "+userid+">\nbacking-store  /dev/cloudvg/" + userid + "\ninitiator-address  "+cl_ip+" \n</target>")

f.close()

commands.getstatusoutput('sudo systemctl restart tgtd')
print "=========================you are done=============================="



