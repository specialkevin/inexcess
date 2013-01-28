import inexcess

from pymongo import MongoClient
import gridfs

def connect():
    mongo_settings = dict(inexcess.read_config('mongo'))
    user = mongo_settings['user']
    port = mongo_settings['port']
    host = mongo_settings['url']
    password = mongo_settings['pass']
    db = mongo_settings['db']
    uri = 'mongodb://'+user+':'+password+'@'+host+':'+port+'/'+db

    database = MongoClient(uri)[db]
    database.authenticate(user,password)
    return database

def uploadFile(filepath, collection):
    database = connect()
    filesystem = gridfs.GridFS(database, collection=collection)
    with open(filepath) as backup_file:
        oid = filesystem.put(backup_file, filename=backup_file)

