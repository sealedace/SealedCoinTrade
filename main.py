# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os
import time
import sys
from Utilities import real_path

__author__ = 'gaoqiangxu'


log_file = open(real_path("log_"+time.strftime("%Y%m%d")+".txt"), 'ab')

def main():

    root_dir = real_path(time.strftime("%Y-%m-%d"))
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)


if __name__ == "__main__":
    main()
