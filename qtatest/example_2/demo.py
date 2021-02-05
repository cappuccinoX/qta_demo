# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2021/02/01 QTAF自动生成

from testbase import datadrive
from testbase.testcase import debug_run_all
from qtalib.testcase import QtaTestCase

test_1_data = [
    {'name': 'Ann', 'age': 18, '__attrs__': {'priorrty': QtaTestCase.EnumPriority.Low}},
    {'name': 'Andy', 'age': 20, '__attrs__': {'__doc__': '第二份data'}}
]
@datadrive.DataDrive(test_1_data)
class Test_1(QtaTestCase):
    ''' Test_1
    '''
    owner = "Michael"
    timeout = 5
    priority = QtaTestCase.EnumPriority.High
    status = QtaTestCase.EnumStatus.Design

    def run_test(self):
        print('name is %s and age is %d' % (self.casedata['name'], self.casedata['age']))
        print(self.priority)

if __name__ == '__main__':
    debug_run_all()
