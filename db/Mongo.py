#
# Mongo.java This is a class for connecting to mongodb 
# @author Cedric Izabayo
#

from pymongo import MongoClient

class Mongo:
    def __init__(self,connection_string):
        self.connection = MongoClient(connection_string)
    
    def getConnection(self):
        return self.connection

#Main execution
def main():
    test_conn = Mongo("mongodb://localhost/Kurious")
    client = test_conn.getConnection()
    # post = client.db.users.find()
    print(client.list_database_names())
    
main()