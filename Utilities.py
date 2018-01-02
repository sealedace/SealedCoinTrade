# -*- coding: utf-8 -*-
__author__ = 'sealedace'

from urllib import quote_plus
import os

def urlencode(val):
    if isinstance(val, unicode):
        return quote_plus(val.encode('utf8'))

    return quote_plus(val)

def real_path(file_name):
    return (os.path.dirname(os.path.realpath(__file__)) + '/' + file_name)
