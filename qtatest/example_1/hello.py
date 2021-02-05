# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2021/02/01 QTAF自动生成

from testbase import datadrive
from testbase.testcase import debug_run_all
from qtalib.testcase import QtaTestCase
from testbase.retry import Retry

test_1_data = [{'name': 'Ann', 'age': 18}, {'name': 'Andy', 'age': 20}]

class TestBase(QtaTestCase):
    def pre_test(self):
        print('pre_test...')
        return super().pre_test()

    def post_test(self):
        print('post_test...')
        return super().post_test()


class HelloTest(TestBase):
    '''示例测试用例
    '''
    owner = "Michael"
    timeout = 5
    priority = QtaTestCase.EnumPriority.High
    status = QtaTestCase.EnumStatus.Design
    tags = 'demo', 'help'
    a = 0

    def string_combain(self, a, b):
        return a + b

    def run_test(self):
        self.start_step('step 1')
        self.assert_('测试__string_combain函数', self.string_combain('x', 'y') == 'xy')
        self.start_step('step 2')
        # self.assert_('测试失败', False)
        self.start_step('step 3')
        for item in Retry(timeout = 2, interval = 0.5):
            print('start to retry...')
            self.a += 1
            if self.a > 2:
                print('a', self.a)
                break

@datadrive.DataDrive(test_1_data)
class Test_1(TestBase):
    ''' Test_1
    '''
    owner = "Michael"
    timeout = 5
    priority = QtaTestCase.EnumPriority.High
    status = QtaTestCase.EnumStatus.Design

    def run_test(self):
        print(self.casedata['name'], self.casedata['age'])

class Test_2(TestBase):
    ''' Test_2
    '''
    owner = "Michael"
    timeout = 5
    priority = QtaTestCase.EnumPriority.High
    status = QtaTestCase.EnumStatus.Design

    def run_test(self):
        print('Test_2')


if __name__ == '__main__':
    debug_run_all()
