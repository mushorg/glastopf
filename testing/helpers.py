from pymongo import MongoClient
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
import bson
import uuid
import json


def populate_mongo_testdata():
        db_name = 'glastopf-test-{0}'.format(str(uuid.uuid4())[0:10])
        c = MongoClient('localhost', 27017)

        #read and insert test data into mongodb instance
        data = open('testing/data/events_500.bson', 'r').read()
        for item in bson.decode_all(data):
            del item['_id']
            c[db_name].events.insert(item)
        return db_name


def populate_main_sql_testdatabase(engine):

    meta = MetaData()

    table = Table('events', meta,
          Column('id', Integer, primary_key=True, ),
          Column('time', String),
          Column('source', String),
          Column('request_method', String),
          Column('request_url', String),
          Column('request_parameters', String),
          Column('request_version', String),
          Column('request_header', String),
          Column('request_body', String),
          Column('pattern', String),
          Column('filename', String),
          Column('response', String),
          )

    meta.create_all(engine)

    insert_dicts = []
    data = open('testing/data/events_500.bson', 'r').read()
    for entry in bson.decode_all(data):

        for key, value in entry['request'].items():
            entry['request_' + key] = value

        entry['source'] = (entry['source'][0] + ":" + str(entry['source'][1]))
        entry['request_header'] = json.dumps(entry['request_header'])
        entry['request_parameters'] = entry['request_parameters'][0]
        del entry['request']
        del entry['_id']
        insert_dicts.append(entry)

    conn = engine.connect()
    print "Inserted: {0}".format(len(insert_dicts))
    conn.execute(table.insert(), insert_dicts)

def delete_mongo_testdata(dbname):
        connection = MongoClient('localhost', 27017)
        connection.drop_database(dbname)


def create_empty_main_db_sqla(engine):
        meta = MetaData()

        Table('events', meta,
              Column('id', Integer, primary_key=True, ),
              Column('time', String),
              Column('source', String),
              Column('request_method', String),
              Column('request_url', String),
              Column('request_parameters', String),
              Column('request_version', String),
              Column('request_header', String),
              Column('request_body', String),
              Column('pattern', String),
              Column('filename', String),
              Column('response', String),
              )

        meta.create_all(engine)


def gen_config(mongodb=None, sql_connectionstring=None):
    """
    Generates configuration for testing purposes.
    """
    return [
            "[dork-db]\n",
            "enabled = True\n",
            "pattern = rfi\n",
            "token_pattern = /\w+\n",
            "n_clusters = 10\n",
            "max_iter = 10\n",
            "n_init = 2\n",
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
            "[main-database]\n",
            "enabled = True\n",
            "connection_string = sqlite:///\n",
            ]

if __name__ == '__main__':
    engine = create_engine('sqlite:///')
    populate_main_sql_testdatabase(engine)
