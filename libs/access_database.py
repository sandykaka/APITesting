"""
database access
~~~~~~~~~~~~~~~
    this help to get the data from database
"""
from collections import namedtuple
from logging import Logger
from pymongo import MongoClient
from pymongo.uri_parser import parse_uri
from pymongo.errors import ConnectionFailure
from pymongo.errors import OperationFailure

Container = namedtuple('Container', 'host user password')

def set_database_values(host_name, env):
    """
    set the database values to access the database
    :param host_name: name of the host e.g. cops, live
    :return: return the namedtuple
    """
    Logger.logr.debug("setting database values")
    if env == 'dev':
        if host_name == 'localhost':
            dbvalue = Container(
                host='localhost',
                username='',
                password=''
            )
        else:
            raise ValueError ("host_name not found in test")
    if env == 'test':
        if host_name == 'testdb':
            dbvalues = Container(
                    host='testhost',
                    user='testuser',
                    password='testuser'
            )
        else:
            raise ValueError ("host_name not found in test")

    if env == 'prod':
        if host_name == 'proddb':
            dbvalues = Container(
                    host='prodhost',
                    user='produser',
                    password='prodpass'
            )
        else:
            raise ValueError ("host_name not found in production")

    Logger.logr.info("database values set as {}".format(dbvalues))
    return dbvalues

class DBConnector(object):

    def __init__(self, dbhost='localhost', dbuser='roo', dbpassword='', database='', dport='27017', env='test'):
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
        if not dbhost:
            raise ValueError ("dbhost value is null")
        if not database:
            self.__database = dbhost
        elif dbhost and dbuser and dbpassword:
            self.__dbhost = dbhost
            self.__dbuser = dbuser
            self.__dbpassword = dbpassword
            self.__dbport = dport
        else:
            raise ValueError ("database/user/password not found")
        #connecting with the database
        self.__connection = None
        self.__session = None
        #self._open()

    #Open connection with database
    def _open(self):
        """
         Creates a database connection and returns
        :return:
        """
        try:

            Logger.logr.debug("trying to connect with database")
            dbURI = "mongodb://"+ self.__dbuser + ":" + self.__dbpassword + "@" + self.__dbhost + ":" + self.__dbport
            cnx = MongoClient(dbURI)
            uri_parts = parse_uri(dbURI)
            dbmongo = cnx[uri_parts[self.__database]]
            dbmongo.authenticate(uri_parts[self.__dbuser], uri_parts[self.__dbpassword])
            self.__connection = dbmongo
        except ConnectionFailure, e:
            Logger.logr.debug(e.args)
            Logger.logr.debug('ERROR: %d: %s' % (e.args[0], e.args[1]))
        Logger.logr.info("connection established to host {} ...".format(self.__dbhost))

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
        :param query: query e.g. 'select * from commerce.returns_label'
        :return: return the results in dictionary
        """
        result_set = {}
        db_name = self.__database   #Name of the table use as key
        Logger.logr.debug("host = {} \n db = {}".format(self.__dbhost, self.__database))
        #getting the table name using regx
        try:
            db_conn = self.__connection
            cnx = db_conn.db_name.collection_name
            result_set = cnx.find()
            return result_set
        except OperationFailure, e:
            raise e

    def __del__(self):
        """
        Closing the connection when this exit
        :return:
        """
        self._close()





