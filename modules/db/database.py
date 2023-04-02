##
## Author: Christopher Pulst
## Date: 3/29/2023
## Version: 1.0
##
## Python: 3.11
##
## Description:
## Handles connection to SQLite database
##

import sqlite3

# Database Connection
class DBConnect:
    def __init__(self):
        pass
    
    def connect(self):
        print("connect called")
        self.con = sqlite3.connect("history.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS History(value1 INT, operator TEXT, value2 INT, result FLOAT);")
        print("History table created")
        
        return self.con
    
    def deleteTable(self):
        self.cursor.execute("DROP TABLE History")
        return
    
    def createEntry(self, value1, operator, value2, result):
        self.cursor.execute("INSERT INTO History (value1, operator, value2, result) VALUES(?,?,?,?)",(value1,operator,value2,result))
        return
    
    def fetchData(self):
        vals = self.cursor.execute("SELECT * FROM History").fetchall()
        return vals
    
    def close(self):
        self.con.close()
    
    def test(self, phrase):
        print("Test this!", phrase)
        return
    
newDB = DBConnect()
newDB.connect()
newDB.createEntry(152, "*", 1, 152)
newDB.createEntry(12, "-", 13, -1)
newDB.createEntry(2018, "+", 1500, 3518)
print(newDB.fetchData())
newDB.close()