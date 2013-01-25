import inexcess
from inexcess import mongo

def backupFiles():
    backup_paths = inexcess.read_config('paths')
    print backup_paths
    for key, path in backup_paths:
        mongo.uploadFile(path, 'files')
    return
