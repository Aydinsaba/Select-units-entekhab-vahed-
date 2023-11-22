#import sqlite3

#cnt=sqlite3.connect("unversit.db")
#-----------create tablet-------------
#sql='''CREATE TABLE student(
 #       id INTEGER PRIMARY KEY,
  #      user VARCHAR(20) NOT NULL,
   #     pas VARCHAR(30) NOT NULL)'''
#cnt.execute(sql)
#print("don")
#-------------units tabel----------
#sql='''CREATE TABELE units(
     #  id INTEGER PRIMARY KEY,
    #   studies VARCHAR(25) NOT NULL,
   #    number VARCHAR(35) NOT NULL,
  #     time VARCHAR(40)NOT NULL,
 #      teacher VARCHAR NOT NULL) '''
#cnt.execute(sql)
#for i in range(15): 
 #   studies=input('s:')
  #  number=int(input('n:'))
   # time=input('t:')
    #teacher=input('t:')
    
   # sql='''INSERT INTO units(studies,number,time,teacher)
    #        VALUES(?,?,?,?)'''
    #cnt.execute(sql,(studies,number,time,teacher))