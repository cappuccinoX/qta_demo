from qtatest.httpapi import Web_API
from qtalib.testcase import QtaTestCase

class TestHttp(QtaTestCase):
    '''http demo
    '''
    owner = "Michael"
    timeout = 5
    priority = QtaTestCase.EnumPriority.High
    status = QtaTestCase.EnumStatus.Design

    def run_test(self):
        self.start_step('发送请求并获取返回包')
        httpReq = Web_API()
        email_template = httpReq.post_web_api(
            'wehr.qq.com',
            '/Center/Organization/getMailContent',
            {
                'examcode': 'F4B859A3BFFFD39CB299',
            }
        )
        print(email_template['content'])
        self.assert_('返回码错误', email_template['status_code'] == 200)    