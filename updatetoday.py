import re
import MySQLdb


class Task:
	def __init__(self):
		db = MySQLdb.connect("localhost","root","asm123","my_bnrk" )
		cursor = db.cursor()
	
		file = open('/home/asm/Documents/nirmal/a1.txt','r').read()
	

		aname = re.compile(r'\s*Name\s*:\s*(.*)')
		cnam = re.findall(aname,file)
		for na in cnam:
			print na
	
		stat = re.compile(r'\s*State\s*:\s*(.*)')
		sta = re.findall(stat,file)
		for st in sta:
			print st
		
		tunn = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/')
		tun = re.findall(tunn,file)
		for tu in tun:
			print tu

		seco = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
		sec = re.findall(seco,file)
		for se in sec:
			s = se.split('/')
			print s[1]

		mesh = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
		mes = re.findall(mesh,file)
		for me in mes:
			print me

		psks = re.compile(r'\s*PSK\s*:\s*(.*)')
		psk = re.findall(psks,file)
		for ps in psk:
			print ps
	
		time = re.compile(r'\s*Timer\s*:\s*(.*)')
		tim = re.findall(time,file)
		for ti in tim:
			print ti
	
		hwsw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)/')	
		hws = re.findall(hwsw,file)
		for hw in hws:
			print hw

		swhw = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
		swh = re.findall(swhw,file)
		for sw in swh:
			s = sw.split('/')
			print s[1]	
	
		mode = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)/')
		mod = re.findall(mode,file)
		for mo in mod:
			print mo
	
		seri = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
		ser = re.findall(seri,file)
		for se in ser:
			s = se.split('/')
			print s[1]
	
		macadd = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
		mac = re.findall(macadd,file)
		for ma in mac:
			print ma

	
		ipv4 = re.compile(r'/\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s/')
		bipv = re.findall(ipv4,file)
		for bip in bipv:
			print bip

	
		ipv6 = re.compile("[a-f0-9]{4}::[0-9]{1}")
		aipv = re.findall(ipv6,file)
		for aip in aipv:
			print aip
		print 'k'
		#if len(cnam)==len(sta)==len(tun)==len(sec)==len(mes)==len(psk)==len(tim)==len(hws)==len(swh)==len(mod)==len(ser)==len(mac)==len(bipv)==len(aipv):
			#print 'l'
		for i in range(len(mac)):
                       	cursor.execute("""INSERT INTO apt
(MACAdddress,IPV4Address,IPv6Address,Name,State,Tunnel,Sec_Mode,Mesh_Role,PSK,Timer,HW_Version,SW_Version,Model,Serial_number) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');""" % (mac[i],bipv[i][1:-1],aipv[i],cnam[i],sta[i],tun[i],mod[i],mes[i],psk[i],tim[i],hws[i],swh[i][11:23],sec[i][15:18],ser[i][9:21]))
			db.commit()

Task()














	












