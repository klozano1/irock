# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 10:50:23 2017

@author: Kamid
"""
import sshtunnel
import mysql.connector
from urllib.parse import quote
from urllib.request import urlopen
import json

#informacion de servidor y base de datos
_host = 'irock.enroute.xyz'
_ssh_port = 22
_username = 'kmarcell'
_password = 'k4m1dM4rc3ll!'


_remote_bind_address = 'localhost'
_local_mysql_port = 9990
_local_bind_address = '127.0.0.1'

_remote_mysql_port = 3306

_db_user = 'kmarcell'
_db_password = 'k4m1dM4rc3ll!'
_db_name = 'kmarcell'


#lee el archivo dir y lo guarda en un arreglo
with open("dir.txt", "r") as ins:
    dirarray = []
    for line in ins:
        dirarray.append(line)
        
#print(dirarray)

service='geocode'
output='json'
paramet='address'


# accesa al url 
variable=[]
qdirarray=[]
for x in range(len(dirarray)):
    qdirarray.append( quote(dirarray[x]))
    u=('https://maps.googleapis.com/maps/api/' + service +'/' + output +'?' + paramet +'='+ qdirarray[x] ) 
    ur=urlopen(u) 
    resp=ur.read().decode('utf-8')
    variable.append(json.JSONDecoder().decode(resp))
   # print(variable[x])
y='OK'
z=0
for x in variable:
    if x['status'] == y:
        archivo=open('results.txt','a')
        print( x['results'][0]['formatted_address']  , file=archivo)
        print( x['results'][0]['geometry']['location']['lat'] , file=archivo)
        print( x['results'][0]['geometry']['location']['lng'] , file=archivo)
        archivo.close()

        _SQL="""insert into resultado (direccion ,latitud, longitud) values ( """ +'"' + x['results'][0]['formatted_address'] +'"'  + ',"'+ str(x['results'][0]['geometry']['location']['lat']) + '"' + ',"' +  str(x['results'][0]['geometry']['location']['lng']) + '")' 
      #  print(_SQL)
        with sshtunnel.SSHTunnelForwarder(
                (_host, _ssh_port),
                ssh_username=_username,
                ssh_password=_password,
                remote_bind_address=(_remote_bind_address, _remote_mysql_port),
                local_bind_address=(_local_bind_address, _local_mysql_port)
            ) as tunnel:
            conn = mysql.connector.connect(
                    user=_db_user,
                    password=_db_password,
                    host=_local_bind_address,
                    database=_db_name,
                    port=_local_mysql_port)
            cursor = conn.cursor()
            cursor.execute(_SQL)
            conn.commit()
            cursor.close()
            conn.close()
                    
        
    else:
        error=open('error.txt','a')
        print( dirarray[z] + x['status']   , file=error)
        error.close()
        
        _SQL2="""insert into errores 
        (ubicacion ,status) 
        values ( """ +'"' + dirarray[z] +   '"' + ' ,' + '"' + x['status'] + '"' ')'
        
       # print (_SQL)
        
        with sshtunnel.SSHTunnelForwarder(
                (_host, _ssh_port),
                ssh_username=_username,
                ssh_password=_password,
                remote_bind_address=(_remote_bind_address, _remote_mysql_port),
                local_bind_address=(_local_bind_address, _local_mysql_port)
            ) as tunnel:
            conn = mysql.connector.connect(
                    user=_db_user,
                    password=_db_password,
                    host=_local_bind_address,
                    database=_db_name,
                    port=_local_mysql_port)
            cursor = conn.cursor()
            cursor.execute(_SQL2)
            conn.commit()
            cursor.close()
            conn.close()
       
    z+=1
print("listo")

    