#!/usr/bin/python
# -*- coding: utf-8 -*-

#we need psycopg2
import psycopg2

#var used to create a string of connection
sDbName = 'mydb'
iDbPort = 5432
sDbUser = 'myuser'
sDbPass = 'passwd'
sDbHost = 'localhost'

#connection
sStrConnect = "dbname=%s user=%s \
               password=%s host=%s \
               port=%i" % (sDbName, sDbUser, sDbPass, sDbHost, iDbPort)
               
con = psycopg2.connect(sStrConnect)

#see documentation here http://initd.org/psycopg/docs/extensions.html#isolation-level-constants
con.set_isolation_level(0)

#create a cursor to work with connection
cur = con.cursor()

sql = """SELECT number, toto, titi 
         FROM bar 
         WHERE foo="%s";
      """

#always give a list !!!
values = (sVar,)

cur.execute(sql, values)

#just one result
res = cur.fetchone()

#many result
res = cur.fetchall()

#if there is a result
if res:
    #do stuff here
    for row in res:
        #load first column into lstNum (if column content is not null)
        lstNum = [num[0] for num in res if num[0] ]
        #etc...
    
    
#commit (for insert and update) and close connexion
con.commit()
con.close()
