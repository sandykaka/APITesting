"""
database access
~~~~~~~~~~~~~~~
    this help to get the data from database
"""
from logging_conf import Logger
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import OperationFailure

class DBConnector(object):

    def __init__(self, dbhost='localhost:27017', dbuser='', dbpassword='', database=''):
        """
        Creates an instance to form and execute a MongoDB statement.
        :param dbhost: host of the database e.g.
        uri = "mongodb://username:password@example.com:27017"
        :param dbuser: username
        :param dbpassword: password
        :param database: name of the database e.g. 'example' or 'rsap'
        :return:
        """
        #Checking the value of dbhost and env
        # Checking the value of dbhost and env
        if not database:
            raise ValueError ("Database value not found, please provide database name")
        self.__dbhost = dbhost
        self.__dbuser = dbuser
        self.__dbpassword = dbpassword
        self.__database = database
        try:
            if dbhost == 'localhost:27017':
                mongo_url = dbhost
            else:
                mongo_url = "mongodb://{username}:{password}@{host}/{database}".format(username=dbuser, password=dbpassword, host=dbhost, database=database)
            cnx = MongoClient(mongo_url)
        except Exception as ex:
           Logger.logr.info("Error", ex)
           raise ConnectionFailure ("Not able to connect to db")

        # Connect to db
        self.__database = cnx.get_database(database)

    #Closing the database connection
    def _close(self):
        """
        Close the session and connection with the database
        :return:
        """
        self.__connection.close()
        self.__session.close()

    #Select query
    def find_all(self, collection_name):
        """
        Run the query passed as 'query' parameter
        :param query: name of the collection from where data need to be fetch
        :return: return the results in dictionary
        """
        db_name = self.__database   #Name of the table use as key
        Logger.logr.debug("host = {} \n db = {}".format(self.__dbhost, self.__database))
        #getting the table name using regx
        try:
            db_collection = db_name.get_collection(collection_name)
            return db_collection.find()
        except OperationFailure, e:
            raise e

    def __del__(self):
        """
        Closing the connection when this exit
        :return:
        """
        self._close()





