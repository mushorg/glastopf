from pymongo import MongoClient
import bson
import uuid


def populate_mongo_testdata():
        db_name = 'glastopf-test-{0}'.format(str(uuid.uuid4())[0:10])
        c = MongoClient('localhost', 27017)

        #read and insert test data into mongodb instance
        data = open('testing/data/events_500.bson', 'r').read()
        for item in bson.decode_all(data):
            del item['_id']
            c[db_name].events.insert(item)
        return db_name


def delete_mongo_testdata(dbname):
        connection = MongoClient('localhost', 27017)
        connection.drop_database(dbname)


def gen_config(mongodb=None, sql_connectionstring=None):
    """
    Generates configuration for testing purposes.
    """
    return ["[sql]\n",
            "enabled = {0}\n".format(True if sql_connectionstring else False),
            "connection_string = {0}\n".format(sql_connectionstring),
            "[dork-db]\n",
            "dork_db = db/dorks.json\n",
            "enabled = True\n",
            "pattern = rfi\n",
            "token_pattern = /\w+\n",
            "n_clusters = 10\n",
            "max_iter = 10\n",
            "n_init = 2\n",
            "[mongodb]\n",
            "enabled = {0}\n".format(True if mongodb else False),
            "host = localhost\n",
            "port = 27017\n",
            "user = a\n",
            "password = b\n",
            "database = {0}\n".format(mongodb),
            "collection = events\n",
            "[surfcertids]\n",
            "enabled = False\n",
            "host = localhost\n",
            "port = 5432\n",
            "user =\n",
            "password =\n",
            "database = idsserver\n",
            "[syslog]\n",
            "enabled = False\n",
            "socket = /dev/log\n",
            "[mail]\n",
            "enabled = False\n",
            "patterns = rfi,lfi\n",
            "user =\n",
            "pwd =\n",
            "mail_from =\n",
            "mail_to =\n",
            "smtp_host = smtp.gmail.com\n",
            "smtp_port = 587\n",
            "[hpfeed]\n",
            "enabled = True\n",
            "host = hpfeeds.honeycloud.net\n",
            "port = 10000\n",
            "secret = 3wis3l2u5l7r3cew\n",
            "chan = glastopf.events,glastopf.files\n",
            "ident = x8yer@hp1\n",
            "[webserver]\n",
            "host = 0.0.0.0\n",
            "port = 8080\n",
            "uid = nobody\n",
            "gid = nogroup\n",
            "proxy_enabled = False\n",
            ]
