#coding=utf8

import sys
import os


def rename_dir(dir_name):
    if os.path.exists(dir_name):
        print("{} exists".format(dir_name))
    
    files = os.listdir(dir_name)
    for f in files:
        #print(f)
        os.rename(f, f + ".re")
    
    print(os.listdir(dir_name))


if __name__ == '__main__':
    dir_name = sys.argv[1]
    rename_dir(dir_name)
