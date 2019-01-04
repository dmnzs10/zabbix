# -*- coding: utf-8 -*-
# Exemplos:
# https://pt.slideshare.net/JanssenLima/como-programar-a-api-do-zabbix

from zabbix_api import ZabbixAPI

zabbix_server = "http:///zabbix"
username = ""
password = ""

#conexao = ZabbixAPI(server = zabbix_server, log_level=6)
conexao = ZabbixAPI(server = zabbix_server)
conexao.login(username, password)

mapa_id = conexao.map.get({
    "search": {"name": ""},
    "output": ["sysmapids","name"]
  })

for x in mapa_id:
    print "Ajustando mapa:",x['sysmapid'], "-", x['name'].encode('utf-8')
    #print x['sysmapid']
    #break
    fix_perm = conexao.map.update({
	"sysmapid": x['sysmapid'],
	#"sysmapid": "653",
	"userGroups": [
	    {"usrgrpid": "13", "permission": "3"},
	    {"usrgrpid": "14", "permission": "3"},
	    {"usrgrpid": "16", "permission": "2"},
	    {"usrgrpid": "17", "permission": "2"},
	    {"usrgrpid": "18", "permission": "2"},
	    {"usrgrpid": "20", "permission": "2"},
	    {"usrgrpid": "23", "permission": "2"},
	    {"usrgrpid": "24", "permission": "2"},
	    {"usrgrpid": "25", "permission": "2"}
	  ]
	})
