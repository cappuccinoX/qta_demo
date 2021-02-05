# -*- coding: utf-8 -*-
'''
项目管理和辅助工具
'''
#2021/02/01 QTAF自动生成

import sys
import os

PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJ_ROOT not in sys.path:
    sys.path.insert(0, PROJ_ROOT)
EXLIB_DIR = os.path.join(PROJ_ROOT, 'exlib')
if os.path.isdir(EXLIB_DIR):
    for filename in os.listdir(EXLIB_DIR):
        if filename.endswith('.egg'):
            lib_path = os.path.join(EXLIB_DIR, filename)
            if os.path.isfile(lib_path) and lib_path not in sys.path:
                sys.path.insert(0, lib_path)

from testbase.management import ManagementTools
# from testbase.loader import TestLoader
if __name__ == '__main__':
    # loader = TestLoader()
    # for it in loader.load('qtatest.hello.Test_1'):
    #     print(it)
    ManagementTools().run()
