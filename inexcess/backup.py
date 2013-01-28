import os
import itertools

import inexcess
from inexcess import mongo


def backupFiles():
    backup_paths = inexcess.read_config('paths')
    for key, path in backup_paths:
        #THIS CRAZY HACK LOOKING THING IS TO GET ME ALL THE FILES
        files = ["{}/{}".format(root, file) for root,file in list(itertools.chain(*[list(itertools.product([root], files)) for root, dirs, files in os.walk(path)]))]
        for single_file in files:
            mongo.uploadFile(single_file, 'files')
    return
