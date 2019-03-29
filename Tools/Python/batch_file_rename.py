#coding=utf8

import sys
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def rename_dir(dir_name):
    if not os.path.exists(dir_name):
        logger.error("{} exists".format(dir_name))
        return
    
    files = os.listdir(dir_name)
    files = [dir_name + os.sep + x for x in files]

    for f in files:
        nf = f + ".re"
        os.rename(f, nf)
        logging.info("{} has been changed to {}".format(f, nf))
    
    print(os.listdir(dir_name))


if __name__ == '__main__':
    dir_name = sys.argv[1]
    rename_dir(dir_name)
