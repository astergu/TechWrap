import os
import sys
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_dir(dir_name):
    if not os.path.exists(dir_name) or os.path.isfile(dir_name):
        os.makedirs(dir_name)
        logging.info("Directory {} created!".format(dir_name))


if __name__ == '__main__':
    dir_name = sys.argv[1]
    create_dir(dir_name)