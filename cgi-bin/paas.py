#!/usr/bin/python

import cgitb,cgi,commands,pwd

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
usr = data.getvalue("userid")
passwd = data.getvalue("password")
pf = data.getvalue("pf")
commands.getstatusoutput("sudo systemctl restart shellinaboxd")
if usr != None and passwd != None: 
	commands.getstatusoutput("sudo useradd -s /usr/bin/" + pf + " \t " + usr)
	commands.getstatusoutput("sudo echo -e " + passwd + " | sudo passwd " + usr + " --stdin")
else:
	print "Don't leave fields empty"

l = """<html>
	<p><a href="https://192.168.112.162:4200"> click to continue </a></p>
	</html> """



print l


