import sqlite3 as lite
import sys
import csv
import pandas as pd
import numpy as np


# function to create the database

def save2db(db_name):
    try:



        con = lite.connect(db_name)
        con.text_factory = str

        with con:

            cur = con.cursor()

            cur.execute("CREATE TABLE PGN(Id INT, PGN INT, PF INT, BytePosition INT, SPN INT)")

            with open('PGNSPNCALCDICT.csv', newline='') as csvfile:
                linereader = csv.reader(csvfile)
                line =1
                for row in linereader:
                    print(line,row[0],row[1],row[2],row[4])
                    statement='INSERT INTO PGN VALUES('+str(line)+','+row[0]+','+row[1]+','+row[2]+','+row[4]+')'
                    print(statement)
                    cur.execute(statement)
                    line +=1

        cur = con.cursor()

        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()

        print("SQLite version: %s" % data)


    finally:
        if con:
            con.close()


## Main code starts here


def get_spn(pgn,bytespos):

    query = "write the query"

    con = lite.connect(db_name)

    with con:
        cur = con.cursor()
        cur.execute("SELECT SPN FROM PGN WHERE PGN=65266 and BytePosition=4")

        rows = cur.fetchall()

        for row in rows:
            #print (row[0])
            i=row[0]
            if i in totalspnlist.keys():
                descp = totalspnlist.get(i)
                print("{}:{}".format(i, descp))


    result = 256

    return result



#declare databasename
db_name= 'j1939v1.db'
# calling the createdatabase function
#save2db(db_name)
totalspnlist = pd.read_csv('SPNList.csv', header=None, index_col=0, squeeze=True, dtype={'1':np.int32}).to_dict()

ans=get_spn(0,2)