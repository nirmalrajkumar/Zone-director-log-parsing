import re
file = open('/home/asm/Documents/nirmal/diag.out','rb').read()

class task:

	def __init__(self):

	

		p = re.compile(r'\s*Name\s*:\s*(.*)')
		ok = re.findall(p,file)
		for a in ok:
			print a
	
		p = re.compile(r'\s*State\s*:\s*(.*)')
		ok = re.findall(p,file)
		for a in ok:
			print a
	
		p = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/')
		ok = re.findall(p,file)
			for a in ok:
				print a

		p = re.compile(r'\s*Tunnel/Sec Mode\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
				b = a.split('/')
		
		print b[1]

		p = re.compile(r'\s*Mesh Role\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
				print a

		p = re.compile(r'\s*PSK\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
				print a
	
		p = re.compile(r'\s*Timer\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
				print a
	
		p = re.compile(r'\s*HW/SW Version\s*:\s*(.*)/')	
		ok = re.findall(p,file)
			for a in ok:
				print a

		p = re.compile(r'\s*HW/SW Version\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
				b = a.split('/')
				print b[1]
	
		p = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)/')
		ok = re.findall(p,file)
			for a in ok:
				print a
	
		p = re.compile(r'\s*Model/Serial Num\s*:\s*(.*)')
		ok = re.findall(p,file)
			for a in ok:
			b = a.split('/')
				print b[1]
	
		p = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
		ok = re.findall(p,file)
			for a in ok:
				print a
	
		p = re.compile(re.compile("[1-9]+(?:\.[0-9]+){3}"))
		ok = re.findall(p,file)
			for a in ok:
				print a

	
		p = re.compile("[a-f0-9]{4}::[0-9]{1}")
		ok = re.findall(p,file)
			for a in ok:
				print a


			

a=task()







	












