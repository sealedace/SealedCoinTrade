# -*- coding: utf-8 -*-

#!/usr/bin/env python

import os
import time
import sys
from Utilities import real_path
import HuobiService

__author__ = 'gaoqiangxu'


def main():
    result = HuobiService.get_symbols()
    print result


if __name__ == "__main__":
    main()
