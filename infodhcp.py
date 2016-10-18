# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 2:
	print "Es necesario poner un parametro."

elif sys.argv[1] == "-l":
	dhcp_leases = open('/var/lib/dhcp/dhcpd.leases','r')
	lista = dhcp_leases.readlines( )
	
	if len(lista) < 5:
		print "No hay ips concedidas."
	else:
		print "Concesiones: "
		for i in lista:
			if i[0] == 'l':
				print i.replace("{", " ")
	dhcp_leases.close()

elif len(sys.argv[1]) >= 7 and len(sys.argv[1]) <= 15:
	lista1 = []
	listaip = []
	listamac = []
	listafinal = []

	dhcp_leases = open('/var/lib/dhcp/dhcpd.leases','r')
	for i in dhcp_leases.readlines():
                if 'lease' in i:
 			ip = i.split(" ")
			lista1.append(ip)
	for i in lista1:
		if i[1] not in ['The','This']:
			listaip.append(i[1])
	dhcp_leases.close()

	dhcp_leases = open('/var/lib/dhcp/dhcpd.leases','r')
	for i in dhcp_leases.readlines():
		if 'hardware' in i:
			mac = i.split(" ")
			listamac.append(mac[4].replace(";"," "))
	dhcp_leases.close()

	listafinal.append(zip(listaip, listamac))
	
	for i in listafinal:
		if i[0][0] == str(sys.argv[1]):
			print "La mac es: ",i[0][1]
		
else:
	print "El parametro recibido no es valido"
