import sys

d=open(sys.argv[1],"r").readlines()

for i in range(0,len(d),1):
	if d[i].find("Nmap scan report for") <> -1:
		if d[i+1].find("latency") <> -1:
			#print d[i].split(" ")[-1].rstrip()+"\t",
			a=d[i].split(" ")[-1].rstrip()
			i=i+1
			while d[i].find("Nmap scan report for") == -1:
				if d[i].find("Read data") <> -1:
					exit()
				if d[i].find("open " or "open|filtered ") <> -1:
					print a+":"+d[i].split(" ")[0].rstrip()+"-"+"open "+"\n",
				if d[i].find("open|filtered ") <> -1:
					print a+":"+d[i].split(" ")[0].rstrip()+"-"+"open|filtered"+"\n",	
				i=i+1
			print
		else:
			print d[i].split(" ")[-1].rstrip()+"\t","closed"
