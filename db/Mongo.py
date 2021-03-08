
from pymongo import MongoClient

class Mongo:
    def __init__(self,connection_string,db_name):
        self.connection = MongoClient(connection_string)
        self.db = self.connection[db_name]
    
    def getConnection(self):
        return self.connection
    def getDbObject(self):
        return self.db

#Main execution 
def main():
    test_conn = Mongo("mongodb://localhost", 'Default')
    # client = test_conn.getConnection()
    mydb = test_conn.getDbObject()
    mycol = mydb['users']
    for x in mycol.find():
        print(x)
    
main()