from qt4s.channel.http import HttpChannel
from qt4s.network.areas import LAN

class Web_API(object):
    def __init__(self):
        self.mcduid = '{mcduid}'.format(mcduid = 170603)
        self.scode = 'a128e20f7390401fce04c39206c91b126371c9e1'

    def get_web_api(self, host, port, route = '/', params = {}):
        chan = HttpChannel((host, port))
        rsp = chan.get(route, params)
        return rsp

    def post_web_api(self, host, route = '/', params = {}, port = 80, proto = 'https'):
        chan = HttpChannel((host, port, LAN, proto))
        cookies = {'mcduid': self.mcduid, 'scode': self.scode }
        rsp = chan.post(url_path = route, body = params, cookies = cookies)
        '''
        返回dict, 格式如下
        {
            status_code: 200
            reason: OK
            headers: {xxx: xxx}
            content: {xxx: xxx}
        }
        '''
        return rsp.to_representation()



