import os

import inexcess
from inexcess import mongo


def backupFiles():
    backup_paths = inexcess.read_config('paths')
    for key, path in backup_paths:
        #THIS CRAZY HACK LOOKING THING IS TO GET ME ALL THE FILES
        files = list(itertools.chain(*[files for root, dirs, files in os.walk(path)]))
        for single_file in files:
            mongo.uploadFile(single_file, 'files')
    return
