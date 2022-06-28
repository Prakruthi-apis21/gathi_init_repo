import sqlite3

#Create Database and make connection
class Demographics:
    def __init__(self):
        self.con=sqlite3.connect('GATHI_DB.db')
        self.cur=self.con.cursor()
        self.createTable()

#Creating Table with constraints
    def createTable(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS DEMOGRAPHICS (
	                        REC_NBR INTEGER PRIMARY KEY ,LATITUDE VARCHAR NOT NULL,STATE VARCHAR NOT NULL)""")

#Checking for valid Values
    def insertTable(self,item):

        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
                  'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA','ME', 'MD', 'MA', 'MI',
                  'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                  'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
                  'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        if item[1] in states :
            self.cur.execute(""" INSERT OR IGNORE  INTO DEMOGRAPHICS VALUES(?,?,?)""",item)
            self.con.commit()

#Reading the Data from Table
    def readTable(self):
        self.cur.execute("""SELECT * FROM DEMOGRAPHICS""")
        rows=self.cur.fetchall()
        print("Reading from table")
        print(rows)

    def conClose(self):
        self.cur.close()
        self.con.close()